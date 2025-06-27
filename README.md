# 🥨 GerLang – Die deutsche Programmiersprache

---

**Absender:**
KibaOfficial

**Empfänger:**
Interessierte Entwicklerinnen und Entwickler

**Betreff:**
GerLang – Eine esoterische Programmiersprache nach DIN 5008

**Datum:** 25.06.2025

---

## 1. Einleitung

Sehr geehrte Damen und Herren,

mit diesem Dokument erhalten Sie eine Übersicht über das Projekt **GerLang** – die wohl deutscheste Programmiersprache der Welt. Ziel ist es, eine humorvolle, aber funktionale Sprache zu schaffen, die sich an der deutschen Sprache und DIN 5008 orientiert.

## 2. Projektbeschreibung

GerLang (*German Language for Code*) ist eine esoterische Programmiersprache, die konsequent deutsche Begriffe für alle Sprachkonstrukte verwendet. Sie ist als Satire gedacht, aber voll lauffähig.

## 3. Merkmale

- **Deutsche Keywords:** z. B. `WENN`, `SONST`, `SOLANGE`, `FÜR`, `NIX`, `GANZ`, `KOMMA`, `WORT`, `JAIN`, `DRUCKE`, `ZURÜCK`
- **CLI-Tool:** Ausführung von `.gerl`-Dateien über die Kommandozeile
- **Lexer, Parser, Interpreter:** Alles selbst entwickelt
- **Beispielskripte:** Im Ordner `beispiele/` bzw. `examples/`

## 4. Installation

1. Python 3.10+ installieren
2. Repository klonen
3. Abhängigkeiten installieren (falls nötig)
4. GerLang ausführen:

```powershell
python gerlang.py run beispiele/haupt.gerl
```

Oder als EXE (siehe Abschnitt 7):

```powershell
./dist/gerlc.exe run beispiele/haupt.gerl
```

## 5. Sprachbeispiel

```gerlang
// Funktionsdefinition mit Parametern und Rückgabewert
GANZ fak(n: GANZ) {
    WENN (n <= 1) {
        ZURÜCK 1;
    } SONST {
        ZURÜCK n * fak(n - 1);
    }
}

// Fehlerbehandlung mit VERSUCHE/FANGE
NIX beispiel() {
    VERSUCHE() {
        GANZ x = 5 / 0;
    } FANGE fehler {
        DRUCKE("Fehler: " + fehler);
    }
}

NIX haupt() {
    DRUCKE("Fakultät von 5: " + fak(5));
    beispiel();
    ZURÜCK;
}
```

## 6. Kommandos

- `run <datei.gerl>` – Führt ein GerLang-Programm aus
- `lex <datei.gerl>` – Zeigt die Token-Liste
- `repl` – Startet die interaktive Shell
- `info` – Zeigt Sprachinfos
- `build` – (optional) Baut eine EXE aus dem Projekt

## 7. EXE-Build (optional)

Mit PyInstaller kann eine eigenständige EXE erzeugt werden:

```powershell
pyinstaller --onefile --name gerlc gerlang.py
```

Oder mit der vorhandenen Spezifikationsdatei (`gerlc.spec`):

```powershell
pyinstaller gerlc.spec
```

## 8. Lizenz

MIT-Lizenz. Siehe Datei `LICENSE`.

## 9. Kontakt

Für Rückfragen, Anregungen oder konstruktive Kritik:
- GitHub: [KibaOfficial](https://github.com/KibaOfficial)
- E-Mail: [Kiba@KibaOfficial.net](mailto:kiba@kibaofficial.net)

---

Mit freundlichen Grüßen

KibaOfficial

*Deutsch. Direkt. Deklarativ. – GerLang, die Programmiersprache, die sogar deine Oma versteht!*
