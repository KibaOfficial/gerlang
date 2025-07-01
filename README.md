# 🥨 GerLang – Die deutsche Programmiersprache

> **Moderne deutschsprachige Programmiersprache** mit TypeScript-Style Fehlermeldungen, professioneller Entwicklererfahrung und vollständiger Turing-Vollständigkeit.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/Version-4.0.0-blue.svg)](docs/CHANGELOG.md)
[![Language](https://img.shields.io/badge/Language-Python-green.svg)](https://python.org)

---

## 🚀 Highlights

### ✨ Moderne Sprachfeatures
- 🇩🇪 **Vollständig deutschsprachige Syntax** (`WENN`, `SONST`, `KISTE`, `DRUCKE`)
- 🛡️ **TypeScript-Style Fehlermeldungen** mit präzisen Positionen und Farben
- 📦 **Modulsystem** mit Import/Export (`HOLE ... VON`, `GIBFREI`)
- 🔧 **Robuste Fehlerbehandlung** (`VERSUCHE/FANGE`)
- 📊 **Mehrdimensionale Arrays** und Methoden-System
- 🎨 **String-Interpolation** mit `${variable}` Templates
- 🔢 **Built-in Math-Funktionen** (`WURZEL`, `POTENZ`, `ZUFALLSBEREICH`)
- 💻 **Professionelle Entwicklererfahrung**

### ✅ **Produktionsreif**
- ✅ **Turing-vollständig** mit Rekursion und unbeschränktem Speicher
- ✅ **Call-Stack Tracking** für perfektes Debugging  
- ✅ **Error-Codes** (GL001-GL999) für strukturierte Fehlerbehandlung
- ✅ **Interaktive Ein-/Ausgabe** mit `LESE()` und `DRUCKE()`
- ✅ **String-Interpolation** für moderne String-Formatierung
- ✅ **Math-Funktionen** für praktische Programmierung
- ✅ **VS Code Extension** mit Syntax-Highlighting

---

## 📋 Inhaltsverzeichnis
1. [Quick Start](#-quick-start)
2. [Installation](#-installation)
3. [Sprachfeatures](#-sprachfeatures)
4. [Dokumentation](#-dokumentation)
5. [Beispiele](#-beispiele-1)
6. [CLI-Kommandos](#-cli-kommandos)
7. [Entwicklung & Build](#️-entwicklung--build)
8. [Beitragen](#-beitragen)
9. [Lizenz & Kontakt](#-lizenz--kontakt)
10. [Roadmap & Status](#-roadmap--status)

---

## 🚀 Quick Start

### Dein erstes GerLang-Programm
```gerlang
// hello.gerl
GANZ haupt() {
    DRUCKE("Hallo, Welt! 🌍");
    WORT name = LESE("Wie heißt du? ");
    
    // String-Interpolation verwenden
    DRUCKE("Schön dich kennenzulernen, ${name}!");
    
    // Math-Funktionen testen
    GANZ zufallszahl = ZUFALLSBEREICH(1, 100);
    DRUCKE("Deine Glückszahl heute: ${zufallszahl} ✨");
    
    ZURÜCK 0;
}
```

### Ausführen
```bash
python gerlang.py run hello.gerl
```

### Erwartete Ausgabe
```
GerLang - Die deutsche Programmiersprache
==================================================
🚀 Führe hello.gerl aus...
Hallo, Welt! 🌍
Wie heißt du? Max
Schön dich kennenzulernen, Max!
Deine Glückszahl heute: 42 ✨
```

---

## 📦 Installation

### Voraussetzungen
- **Python 3.10+** installiert
- **Git** für das Klonen des Repositories

### Schritt-für-Schritt
```bash
# 1. Repository klonen
git clone <repository-url>
cd gerlang

# 2. GerLang testen
python gerlang.py run examples/fibonacci.gerl

# 3. Optional: EXE verwenden (Windows)
./bin/gerlc.exe run examples/fibonacci.gerl
```

---

## 🎯 Sprachfeatures

### 🇩🇪 Deutsche Syntax
```gerlang
// Variablen und Datentypen
GANZ alter = 25;                   // Ganzzahl (int)
KOMMA preis = 19.99;              // Kommazahl (float)
WORT name = "Max Mustermann";      // String
JAIN aktiv = JA;                   // Boolean (JA/NEIN)
KISTE zahlen = [1, 2, 3, 4, 5];   // Array

// Kontrollstrukturen
WENN (alter >= 18) {
    DRUCKE("Erwachsen");
} SONST {
    DRUCKE("Minderjährig");
}

SOLANGE (aktiv) {
    DRUCKE("Läuft...");
    aktiv = NEIN;
}
```

### 🛡️ TypeScript-Style Fehlermeldungen
```
Fehler GL006: Division durch Null
  --> test.gerl:6:14
   |
  5 |     GANZ b = 0;
  6 |     ZURÜCK a / b;  // Division durch Null
   |              ^
  7 | }
   |
   Division oder Modulo durch Null ist nicht erlaubt
   = Tipp: Prüfe den Divisor vor der Operation

Call-Stack:
  0: test_division() at test.gerl:15:32
```

### 📦 Modulsystem
```gerlang
// math.gerl - Modul exportieren
GIBFREI GANZ addiere(a: GANZ, b: GANZ) {
    ZURÜCK a + b;
}

// main.gerl - Modul importieren  
HOLE addiere VON "math.gerl";

GANZ haupt() {
    GANZ summe = addiere(5, 3);
    DRUCKE("Summe: " + summe);
    ZURÜCK 0;
}
```

### 🔧 Moderne Features
```gerlang
// String-Interpolation
WORT name = "Max";
GANZ alter = 25;
DRUCKE("Hallo ${name}, du bist ${alter} Jahre alt!");
DRUCKE("Nächstes Jahr wirst du ${alter + 1}!");

// Math-Funktionen
KOMMA radius = 5.0;
KOMMA flaeche = POTENZ(radius, 2) * 3.14159;
DRUCKE("Kreisfläche: ${RUNDEN(flaeche, 2)} cm²");

GANZ wuerfel = ZUFALLSBEREICH(1, 6);
DRUCKE("Würfelwurf: ${wuerfel}");

// Array-Methoden
KISTE liste = [1, 2, 3];
liste.ERWEITERN(4);               // [1, 2, 3, 4]
GANZ anzahl = liste.LÄNGE;        // 4
DRUCKE("Liste hat ${anzahl} Elemente");

// Fehlerbehandlung
VERSUCHE() {
    GANZ result = risiko_operation();
} FANGE fehler {
    DRUCKE("Fehler abgefangen: ${fehler}");
}

// Interaktive Ein-/Ausgabe
WORT eingabe = LESE("Dein Name: ");
DRUCKE("Hallo, ${eingabe}!");
```

---

## 📚 Dokumentation

### 🚀 **Schnellstart**
- 📖 [**SPRACHE.md**](docs/SPRACHE.md) - **Vollständige Sprachreferenz** (empfohlener Einstieg)
- 🎮 [**BEISPIELE.md**](docs/BEISPIELE.md) - **Praxisnahe Code-Beispiele**
- ❓ [**FAQ.md**](docs/faq.md) - **Häufige Fragen & Troubleshooting**

### 📋 **Detaillierte Referenzen**
- 🔢 [**operatoren.md**](docs/operatoren.md) - Arithmetische, logische und Vergleichsoperatoren
- 📝 [**syntax.md**](docs/syntax.md) - Syntax-Regeln und Best Practices
- 🛡️ [**fehlerbehandlung.md**](docs/fehlerbehandlung.md) - Try-Catch und Error-Handling
- 💬 [**ein_ausgabe.md**](docs/ein_ausgabe.md) - DRUCKE(), LESE() und I/O-Funktionen
- 📊 [**arrays.md**](docs/arrays.md) - Mehrdimensionale Arrays und Methoden
- ⚡ [**funktionen.md**](docs/funktionen.md) - Funktionsdefinition und Rekursion
- 📦 [**modulsystem.md**](docs/modulsystem.md) - Import/Export mit HOLE/GIBFREI
- 🔧 [**variablen.md**](docs/variablen.md) - Datentypen und Zuweisungen

### 📈 **Projekt-Information**
- 📅 [**CHANGELOG.md**](docs/CHANGELOG.md) - Versionshistorie und Änderungen
- 📖 [**glossar.md**](docs/glossar.md) - Deutsche Begriffe und Übersetzungen
- 🗝️ [**KEYWORDS.md**](docs/KEYWORDS.md) - Alle reservierten Schlüsselwörter

### 🎯 **Für Entwickler**
- 🏗️ [**SPRACHE_DETAIL.md**](docs/SPRACHE_DETAIL.md) - Technische Implementation
- 🔍 [**kontrollstrukturen.md**](docs/kontrollstrukturen.md) - IF/WHILE/FOR im Detail

---

## 🚀 Beispiele

### Fibonacci-Zahlen
```gerlang
GANZ fibonacci(n: GANZ) {
    WENN (n <= 1) {
        ZURÜCK n;
    }
    ZURÜCK fibonacci(n - 1) + fibonacci(n - 2);
}

GANZ haupt() {
    FÜR (GANZ i = 0; i < 10; i = i + 1) {
        DRUCKE("Fibonacci(" + i + ") = " + fibonacci(i));
    }
    ZURÜCK 0;
}
```

### Interaktives Zahlenraten
```gerlang
GANZ haupt() {
    GANZ geheimzahl = 42;  // TODO: ZUFALLSZAHL() 
    WORT eingabe;
    
    DRUCKE("=== Zahlenraten ===");
    DRUCKE("Ich denke an eine Zahl zwischen 1 und 100!");
    
    SOLANGE (eingabe != "42") {
        eingabe = LESE("Dein Tipp: ");
        
        WENN (eingabe == "42") {
            DRUCKE("🎉 Richtig geraten!");
        } SONST {
            DRUCKE("Leider falsch, versuch es nochmal!");
        }
    }
    
    ZURÜCK 0;
}
```

Weitere Beispiele findest du in:
- 📁 [`examples/`](examples/) - Offizielle Beispielprogramme
- 📖 [`docs/BEISPIELE.md`](docs/BEISPIELE.md) - Detaillierte Tutorials

---

## 🔧 CLI-Kommandos

```bash
# GerLang-Programme ausführen
python gerlang.py run <datei.gerl>
python gerlang.py run examples/fibonacci.gerl

# Entwicklungs-Tools  
python gerlang.py tokens <datei.gerl>    # Token-Analyse
python gerlang.py ast <datei.gerl>       # AST-Struktur anzeigen
python gerlang.py repl                   # Interaktive Shell (TODO)

# Projekt-Information
python gerlang.py info                   # Sprachinfos
python gerlang.py --help                # Hilfe anzeigen
```

### EXE-Version (Windows)
```bash
# Vorkompilierte Version verwenden
./bin/gerlc.exe run examples/fibonacci.gerl

# Eigene EXE erstellen
pyinstaller gerlc.spec
```

---

## 🏗️ Entwicklung & Build

### Repository klonen
```bash
git clone <repository-url>
cd gerlang
```

### EXE-Build mit PyInstaller
```bash
# Einfacher Build
pyinstaller --onefile --name gerlc gerlang.py

# Mit vorgefertigter Spec-Datei
pyinstaller gerlc.spec
```

### Tests ausführen
```bash
# Beispielprogramme testen
python gerlang.py run examples/fibonacci.gerl
python gerlang.py run examples/fizzbuzz.gerl
python gerlang.py run test_runtime_error.gerl

# Error-Handling testen
python gerlang.py run test_undefined_var.gerl
```

---

## 🤝 Beitragen

### Bug Reports & Feature Requests
- 🐛 **Issues** auf GitHub erstellen
- 💡 **Feature-Wünsche** in GitHub Discussions
- 📝 **Dokumentation** verbessern

### Development
```bash
# Code-Stil prüfen
python -m flake8 src/
python -m mypy src/

# Neue Features testen
python gerlang.py run your_test.gerl
```

---

## 📄 Lizenz & Kontakt

### 📜 Lizenz
**MIT-Lizenz** - Siehe [`LICENSE`](LICENSE) Datei

### 💬 Kontakt
- 🐙 **GitHub**: [KibaOfficial](https://github.com/KibaOfficial)
- 📧 **E-Mail**: [Kiba@KibaOfficial.net](mailto:kiba@kibaofficial.net)
- 💡 **Feature-Requests**: GitHub Discussions

---

## 🎉 Roadmap & Status

### ✅ **Vollständig implementiert (v4.0.0)**
- 🇩🇪 Deutsche Syntax und Keywords
- 🛡️ TypeScript-Style Fehlermeldungen  
- 📦 Modulsystem (Import/Export)
- 🔧 Fehlerbehandlung (Try/Catch)
- 📊 Mehrdimensionale Arrays
- 💬 Interaktive Ein-/Ausgabe
- 🎯 Call-Stack und Debugging

### 🔄 **In Entwicklung**
- 🎮 **REPL** (Interactive Shell)
- ️ **Maps/Dictionaries** (KARTE Datentyp)
- 📝 **String-Methoden** (AUFTEILEN, ERSETZEN, ENTHÄLT)
- 🏗️ **Strukturen/Objekte** (ORDNUNG/DING)
- 🔍 **Array-Methoden** (SORTIEREN, FILTERN, FINDEN)

### 🌟 **Zukunft**
- 🚀 **Compiler** (statt Interpreter)
- 📚 **Standardbibliothek**
- 🔌 **LSP** (Language Server Protocol)
- 🎯 **Debugger** mit Breakpoints

---

*Deutsch. Direkt. Deklarativ. – **GerLang**, die Programmiersprache, die sogar deine Oma versteht!* 🥨🚀
