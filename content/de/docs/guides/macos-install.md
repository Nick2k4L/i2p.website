---
title: "I2P auf macOS installieren"
description: "Schritt-für-Schritt-Anleitung zur manuellen Installation von I2P und seinen Abhängigkeiten auf macOS"
lastUpdated: "2025-10"
accurateFor: "2.10.0"
---

## Was Sie benötigen

- Ein Mac mit macOS 10.14 (Mojave) oder neuer
- Administratorrechte zur Installation von Anwendungen
- Etwa 15-20 Minuten Zeit
- Internetverbindung zum Herunterladen der Installationsprogramme

## Überblick

Dieser Installationsvorgang umfasst vier Hauptschritte:

1. **Java installieren** - Laden Sie die Oracle Java Runtime Environment herunter und installieren Sie sie
2. **I2P installieren** - Laden Sie den I2P-Installer herunter und führen Sie ihn aus
3. **I2P-App konfigurieren** - Richten Sie den Launcher ein und fügen Sie ihn zu Ihrem Dock hinzu
4. **I2P-Bandbreite konfigurieren** - Führen Sie den Setup-Assistenten aus, um Ihre Verbindung zu optimieren

## Teil Eins: Java installieren

I2P benötigt Java zum Ausführen. Wenn Sie bereits Java 8 oder höher installiert haben, können Sie [zu Teil Zwei springen](#part-two-download-and-install-i2p).

### Schritt 1: Java herunterladen

Besuchen Sie die [Oracle Java Download-Seite](https://www.oracle.com/java/technologies/downloads/) und laden Sie den macOS-Installer für Java 8 oder höher herunter.

![Oracle Java für macOS herunterladen](/images/guides/macos-install/0-jre.png)

### Schritt 2: Führen Sie das Installationsprogramm aus

Suchen Sie die heruntergeladene `.dmg`-Datei in Ihrem Downloads-Ordner und doppelklicken Sie darauf, um sie zu öffnen.

![Java-Installer öffnen](/images/guides/macos-install/1-jre.png)

### Schritt 3: Installation erlauben

macOS zeigt möglicherweise eine Sicherheitswarnung an, da der Installer von einem identifizierten Entwickler stammt. Klicken Sie auf **Öffnen**, um fortzufahren.

![Geben Sie dem Installer die Berechtigung fortzufahren](/images/guides/macos-install/2-jre.png)

### Schritt 4: Java installieren

Klicken Sie auf **Installieren**, um den Java-Installationsprozess zu starten.

![Java-Installation starten](/images/guides/macos-install/3-jre.png)

### Schritt 5: Auf die Installation warten

Das Installationsprogramm kopiert Dateien und konfiguriert Java auf Ihrem System. Dies dauert normalerweise 1-2 Minuten.

![Warten Sie, bis die Installation abgeschlossen ist](/images/guides/macos-install/4-jre.png)

### Schritt 6: Installation abgeschlossen

Wenn Sie die Erfolgsmeldung sehen, ist Java installiert! Klicken Sie auf **Schließen**, um den Vorgang abzuschließen.

![Java-Installation abgeschlossen](/images/guides/macos-install/5-jre.png)

## Teil Zwei: I2P herunterladen und installieren

Jetzt, da Java installiert ist, können Sie den I2P router installieren.

### Schritt 1: I2P herunterladen

Besuchen Sie die [Downloads-Seite](/downloads/) und laden Sie den **I2P für Unix/Linux/BSD/Solaris** Installer (die `.jar`-Datei) herunter.

![I2P-Installer herunterladen](/images/guides/macos-install/0-i2p.png)

### Schritt 2: Installer ausführen

Doppelklicken Sie auf die heruntergeladene `i2pinstall_X.X.X.jar` Datei. Das Installationsprogramm wird gestartet und Sie werden aufgefordert, Ihre bevorzugte Sprache auszuwählen.

![Select your language](/images/guides/macos-install/1-i2p.png)

### Schritt 3: Willkommensbildschirm

Lesen Sie die Willkommensnachricht und klicken Sie auf **Weiter**, um fortzufahren.

![Installer introduction](/images/guides/macos-install/2-i2p.png)

### Schritt 4: Wichtiger Hinweis

Das Installationsprogramm zeigt einen wichtigen Hinweis zu Updates an. I2P-Updates sind **end-to-end signiert** und verifiziert, obwohl das Installationsprogramm selbst nicht signiert ist. Klicken Sie auf **Weiter**.

![Important notice about updates](/images/guides/macos-install/3-i2p.png)

### Schritt 5: Lizenzvereinbarung

Lesen Sie die I2P-Lizenzvereinbarung (BSD-ähnliche Lizenz). Klicken Sie auf **Weiter**, um zu akzeptieren.

![License agreement](/images/guides/macos-install/4-i2p.png)

### Schritt 6: Installationsverzeichnis auswählen

Wählen Sie aus, wo I2P installiert werden soll. Der Standardort (`/Applications/i2p`) wird empfohlen. Klicken Sie auf **Weiter**.

![Installationsverzeichnis auswählen](/images/guides/macos-install/5-i2p.png)

### Schritt 7: Komponenten auswählen

Lassen Sie alle Komponenten für eine vollständige Installation ausgewählt. Klicken Sie auf **Weiter**.

![Zu installierende Komponenten auswählen](/images/guides/macos-install/6-i2p.png)

### Schritt 8: Installation starten

Überprüfen Sie Ihre Auswahl und klicken Sie auf **Weiter**, um mit der Installation von I2P zu beginnen.

![Installation starten](/images/guides/macos-install/7-i2p.png)

### Schritt 9: Dateien installieren

Das Installationsprogramm wird I2P-Dateien auf Ihr System kopieren. Dies dauert etwa 1-2 Minuten.

![Installation in progress](/images/guides/macos-install/8-i2p.png)

### Schritt 10: Start-Skripte generieren

Das Installationsprogramm erstellt Startskripte zum Starten von I2P.

![Generierung von Start-Skripten](/images/guides/macos-install/9-i2p.png)

### Schritt 11: Installations-Verknüpfungen

Das Installationsprogramm bietet an, Desktop-Verknüpfungen und Menüeinträge zu erstellen. Treffen Sie Ihre Auswahl und klicken Sie auf **Weiter**.

![Create shortcuts](/images/guides/macos-install/10-i2p.png)

### Schritt 12: Installation abgeschlossen

Erfolgreich! I2P ist nun installiert. Klicken Sie auf **Fertig**, um den Vorgang abzuschließen.

![Installation vollständig](/images/guides/macos-install/11-i2p.png)

## Teil Drei: I2P-App konfigurieren

Lassen Sie uns nun I2P einfach zu starten machen, indem wir es zu Ihrem Programme-Ordner und Dock hinzufügen.

### Schritt 1: Anwendungsordner öffnen

Öffnen Sie den Finder und navigieren Sie zu Ihrem **Programme**-Ordner.

![Open the Applications folder](/images/guides/macos-install/0-conf.png)

### Schritt 2: I2P Launcher finden

Suchen Sie nach dem **I2P** Ordner oder der **Start I2P Router** Anwendung in `/Applications/i2p/`.

![Finden Sie den I2P-Launcher](/images/guides/macos-install/1-conf.png)

### Schritt 3: Zum Dock hinzufügen

Ziehen Sie die Anwendung **Start I2P Router** in Ihr Dock für einfachen Zugriff. Sie können auch einen Alias auf Ihrem Desktop erstellen.

![I2P zu Ihrem Dock hinzufügen](/images/guides/macos-install/2-conf.png)

**Tipp**: Klicken Sie mit der rechten Maustaste auf das I2P-Symbol im Dock und wählen Sie **Optionen → Im Dock behalten**, um es dauerhaft zu machen.

## Teil Vier: I2P-Bandbreite konfigurieren

Beim ersten Start von I2P durchlaufen Sie einen Setup-Assistenten, um Ihre Bandbreiteneinstellungen zu konfigurieren. Dies hilft dabei, die Leistung von I2P für Ihre Verbindung zu optimieren.

### Schritt 1: I2P starten

Klicken Sie auf das I2P-Symbol in Ihrem Dock (oder doppelklicken Sie auf das Startprogramm). Ihr Standard-Webbrowser öffnet sich mit der I2P Router Console.

![I2P Router Console Willkommensbildschirm](/images/guides/macos-install/0-wiz.png)

### Schritt 2: Willkommens-Assistent

Der Einrichtungsassistent wird Sie begrüßen. Klicken Sie auf **Weiter**, um mit der Konfiguration von I2P zu beginnen.

![Setup wizard introduction](/images/guides/macos-install/1-wiz.png)

### Schritt 3: Sprache und Theme

Wählen Sie Ihre bevorzugte **Oberflächensprache** und entscheiden Sie zwischen **hellem** oder **dunklem** Design. Klicken Sie auf **Weiter**.

![Sprache und Design auswählen](/images/guides/macos-install/2-wiz.png)

### Schritt 4: Bandbreitentest-Informationen

Der Assistent erklärt den Bandbreitentest. Dieser Test verbindet sich mit dem **M-Lab**-Dienst, um Ihre Internetgeschwindigkeit zu messen. Klicken Sie auf **Weiter**, um fortzufahren.

![Bandwidth test explanation](/images/guides/macos-install/3-wiz.png)

### Schritt 5: Bandbreitentest durchführen

Klicken Sie auf **Test ausführen**, um Ihre Upload- und Download-Geschwindigkeiten zu messen. Der Test dauert etwa 30-60 Sekunden.

![Running the bandwidth test](/images/guides/macos-install/4-wiz.png)

### Schritt 6: Testergebnisse

Überprüfen Sie Ihre Testergebnisse. I2P wird Bandbreiteneinstellungen basierend auf Ihrer Verbindungsgeschwindigkeit empfehlen.

![Bandwidth test results](/images/guides/macos-install/5-wiz.png)

### Schritt 7: Bandbreitenfreigabe konfigurieren

Wählen Sie, wie viel Bandbreite Sie mit dem I2P-Netzwerk teilen möchten:

- **Automatisch** (Empfohlen): I2P verwaltet die Bandbreite basierend auf Ihrer Nutzung
- **Begrenzt**: Bestimmte Upload-/Download-Limits festlegen
- **Unbegrenzt**: So viel wie möglich teilen (für schnelle Verbindungen)

Klicken Sie auf **Weiter**, um Ihre Einstellungen zu speichern.

![Bandbreitenteilung konfigurieren](/images/guides/macos-install/6-wiz.png)

### Schritt 8: Konfiguration abgeschlossen

Ihr I2P router ist jetzt konfiguriert und läuft! Die router-Konsole zeigt Ihren Verbindungsstatus an und ermöglicht es Ihnen, I2P-Seiten zu durchsuchen.

## Erste Schritte mit I2P

Nachdem I2P installiert und konfiguriert ist, können Sie:

1. **I2P-Seiten durchsuchen**: Besuchen Sie die `http://127.0.0.1:7657/home`, um Links zu beliebten I2P-Diensten zu sehen
2. **Browser konfigurieren**: Richten Sie ein [Browser-Profil](/docs/guides/browser-config) ein, um auf `.i2p`-Seiten zuzugreifen
3. **Dienste erkunden**: Entdecken Sie I2P-E-Mail, Foren, Filesharing und mehr
4. **Router überwachen**: Die `http://127.0.0.1:7657/console` zeigt Ihren Netzwerkstatus und Statistiken an

### Nützliche Links

- **Router Console**: `http://127.0.0.1:7657/`
- **Konfiguration**: `http://127.0.0.1:7657/config`
- **Adressbuch**: `http://127.0.0.1:7657/susidns/addressbook`
- **Bandbreiten-Einstellungen**: `http://127.0.0.1:7657/config`

## Setup-Assistenten erneut ausführen

Wenn Sie Ihre Bandbreiten-Einstellungen ändern oder I2P später neu konfigurieren möchten, können Sie den Begrüßungsassistenten über die Router Console erneut ausführen:

1. Gehen Sie zum `http://127.0.0.1:7657/welcome`
2. Folgen Sie den Schritten des Assistenten erneut

## Fehlerbehebung

### I2P startet nicht

- **Java überprüfen**: Stellen Sie sicher, dass Java installiert ist, indem Sie `java -version` im Terminal ausführen
- **Berechtigungen überprüfen**: Stellen Sie sicher, dass der I2P-Ordner die richtigen Berechtigungen hat
- **Logs überprüfen**: Schauen Sie in `~/.i2p/wrapper.log` nach Fehlermeldungen

### Browser kann nicht auf I2P-Sites zugreifen

- Stellen Sie sicher, dass I2P läuft (überprüfen Sie die Router Console)
- Konfigurieren Sie die Proxy-Einstellungen Ihres Browsers, um den HTTP-Proxy `127.0.0.1:4444` zu verwenden
- Warten Sie 5-10 Minuten nach dem Start, damit sich I2P in das Netzwerk integrieren kann

### Langsame Leistung

- Führen Sie den Bandbreitentest erneut durch und passen Sie Ihre Einstellungen an
- Stellen Sie sicher, dass Sie etwas Bandbreite mit dem Netzwerk teilen
- Überprüfen Sie Ihren Verbindungsstatus in der Router Console

## I2P deinstallieren

Um I2P von Ihrem Mac zu entfernen:

1. Beenden Sie den I2P router, falls er läuft
2. Löschen Sie den `/Applications/i2p` Ordner
3. Löschen Sie den `~/.i2p` Ordner (Ihre I2P-Konfiguration und -Daten)
4. Entfernen Sie das I2P-Symbol aus Ihrem Dock

## Nächste Schritte

- **Der Community beitreten**: Besuchen Sie [i2pforum.net](http://i2pforum.net) oder schauen Sie sich I2P auf Reddit an
- **Mehr erfahren**: Lesen Sie die [I2P-Dokumentation](/en/docs), um zu verstehen, wie das Netzwerk funktioniert
- **Mitmachen**: Erwägen Sie, zur [I2P-Entwicklung beizutragen](/en/get-involved) oder Infrastruktur zu betreiben

Herzlichen Glückwunsch! Sie sind jetzt Teil des I2P-Netzwerks. Willkommen im unsichtbaren Internet!

---
