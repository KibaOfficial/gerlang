# v4.0.0 Latest

🥨 GerLang & VS Code Extension – Gemeinsames Release

**GerLang Compiler/Interpreter v4.0.0**  
**VS Code Extension v5.0.0**

## Was ist neu?

### GerLang Compiler/Interpreter (gerlc 4.0.0)

**🛡️ TypeScript-Style Error Handling (VOLLSTÄNDIG):**
- Präzise Positionsangaben für alle Runtime-Fehler (Zeile:Spalte)
- Farbige Fehlermeldungen mit Quellcode-Kontext und Caret-Zeiger (^)
- Error-Codes (GL001-GL999) für bessere Kategorisierung
- Call-Stack mit korrekten Aufrufpositionen
- Hilfreiche Tipps für häufige Fehler
- Vollständige AST-Node Positionserkennung implementiert

**🔢 Built-in Math-Funktionen (VOLLSTÄNDIG):**
- `WURZEL(zahl)` - Quadratwurzel berechnen
- `POTENZ(basis, exponent)` - Potenz berechnen (basis^exponent)
- `ABS(zahl)` - Absolutwert/Betrag
- `RUNDEN(zahl, nachkommastellen=0)` - Zahlen runden
- `ZUFALLSZAHL()` - Zufallszahl zwischen 0.0 und 1.0
- `ZUFALLSBEREICH(min, max)` - Ganzzahl im Bereich min-max

**🎨 String-Interpolation (VOLLSTÄNDIG):**
- Template-Strings mit `${variable}` und `${ausdruck}` Syntax
- Verschachtelte Expressions in Templates möglich
- Methoden-Aufrufe in Templates: `"Du hast ${liste.LÄNGE} Elemente"`
- Komplexe Ausdrücke: `"Nächstes Jahr: ${alter + 1}"`

**🔄 Erweiterte Typ-Konvertierung:**
- `ZU_WORT(wert)`, `ZU_GANZ(wert)`, `ZU_KOMMA(wert)` funktionieren robust
- Bessere Fehlerbehandlung bei ungültigen Konvertierungen

**🐛 Bugfixes:**
- Exception-Handling in CallExpression repariert
- Problem: ZU_GANZ und andere Built-ins wurden als "unbekannte Funktion" in VERSUCHE/FANGE-Blöcken gemeldet
- Jetzt werden korrekte Fehlermeldungen wie "Kann 'abc' nicht zu GANZ konvertieren" angezeigt

**Breaking:**
- Nicht abwärtskompatibel zu 3.x – bitte Code und Doku prüfen!

### VS Code Extension (5.0.0)

**🔍 IntelliSense:**
- Hover-Provider für Built-in Funktionen mit Dokumentation und Beispielen
- Signature Help für Funktionen mit Parameter-Informationen
- Autovervollständigung für alle V4.0 Features (Math-Funktionen, Typ-Konvertierung)

**📝 Snippets:**
- Neue Snippets für String-Interpolation und Template-Strings
- Math-Funktionen und Typ-Konvertierung Snippets
- Template String Demo mit vollständigen Beispielen

**🎨 Syntax-Highlighting:**
- Vollständige Unterstützung für String-Interpolation `${...}`
- Built-in Math-Funktionen werden erkannt und hervorgehoben
- Typ-Konvertierung Funktionen haben eigene Highlighting-Kategorie

**🛠️ Fehlerdiagnose:**
- Verbesserte Fehleranalyse mit V4.0 Error-Codes
- Bessere Parsing von TypeScript-Style Fehlermeldungen

**📚 Dokumentation:**
- Vollständig aktualisierte Beschreibung für V4.0 Features
- Keywords erweitert um neue Funktionalitäten

**🔧 Kompatibilität:**
- 100% kompatibel zu GerLang 4.0.0!

## Hinweise:

- Bitte aktualisiere sowohl die Extension als auch den Compiler, um alle neuen Features nutzen zu können.
- String-Interpolation und Math-Funktionen revolutionieren die Entwicklererfahrung!
- Siehe README.md und die Doku im Ordner docs für Details, Beispiele und Hinweise.
- Feedback und Bugreports sind wie immer willkommen!

**Viel Spaß mit den revolutionären neuen Features und weiterhin frohes Coden auf Deutsch!** 🚀

---

## Assets
- `gerlc.exe` - GerLang 4.0.0 Compiler/Interpreter
- `gerlang-5.0.0.vsix` - VS Code Extension 5.0.0
- Source code (zip/tar.gz)
