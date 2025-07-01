# Changelog für GerLang

## [4.0.0] – 2025-07-01
### 🚀 Major Features & Breaking Changes
- **🛡️ TypeScript-Style Error Handling (VOLLSTÄNDIG):**
  - Präzise Positionsangaben für alle Runtime-Fehler (Zeile:Spalte)
  - Farbige Fehlermeldungen mit Quellcode-Kontext und Caret-Zeiger (^)
  - Error-Codes (GL001-GL999) für bessere Kategorisierung
  - Call-Stack mit korrekten Aufrufpositionen
  - Hilfreiche Tipps für häufige Fehler
  - Vollständige AST-Node Positionserkennung implementiert

- **🔢 Built-in Math-Funktionen (VOLLSTÄNDIG):**
  - `WURZEL(zahl)` - Quadratwurzel berechnen
  - `POTENZ(basis, exponent)` - Potenz berechnen (basis^exponent)
  - `ABS(zahl)` - Absolutwert/Betrag
  - `RUNDEN(zahl, nachkommastellen=0)` - Zahlen runden
  - `ZUFALLSZAHL()` - Zufallszahl zwischen 0.0 und 1.0
  - `ZUFALLSBEREICH(min, max)` - Ganzzahl im Bereich min-max

- **🎨 String-Interpolation (VOLLSTÄNDIG):**
  - Template-Strings mit `${variable}` und `${ausdruck}` Syntax
  - Verschachtelte Expressions in Templates möglich
  - Methoden-Aufrufe in Templates: `"Du hast ${liste.LÄNGE} Elemente"`
  - Komplexe Ausdrücke: `"Nächstes Jahr: ${alter + 1}"`

- **🔄 Erweiterte Typ-Konvertierung:**
  - `ZU_WORT(wert)`, `ZU_GANZ(wert)`, `ZU_KOMMA(wert)` funktionieren robust
  - Bessere Fehlerbehandlung bei ungültigen Konvertierungen
### 🐛 Bugfixes
- **Exception-Handling in CallExpression repariert:**
  - Problem: ZU_GANZ und andere Built-ins wurden als "unbekannte Funktion" in VERSUCHE/FANGE-Blöcken gemeldet
  - Ursache: CallExpression fing alle Exceptions ab, auch echte Ausführungsfehler
  - Lösung: Unterscheidung zwischen "Funktion nicht gefunden" und "Ausführungsfehler"
  - Jetzt werden korrekte Fehlermeldungen wie "Kann 'abc' nicht zu GANZ konvertieren" angezeigt
- Runtime-Fehler zeigten immer Position 1:1 → Jetzt korrekte Zeile:Spalte
- Import-Problem bei Exception-Behandlung behoben
- AST-Node Konstruktoren hatten keine Positionsinformationen
- Call-Stack zeigte falsche Aufrufpositionen

### 💻 Entwicklererfahrung
- Professionelle Fehlermeldungen auf TypeScript-Niveau
- Debugging wird deutlich einfacher durch präzise Fehlerlokalisierung
- Error-Handling ist jetzt vollständig und produktionsreif
- Moderne Built-in Funktionen für praktische Programmierung
- Template-Strings für elegante String-Formatierung

### 📚 Dokumentation
- SPRACHE.md um Built-in Funktionen und detaillierte Beispiele erweitert
- Neue Math-Funktionen in allen relevanten Docs dokumentiert
- Zahlenraten-Beispiel mit modernen Funktionen überarbeitet
- README.md mit funktionierenden Anchor-Links und verbesserter Navigation
- Alle Dokumentationsdateien professionell überarbeitet und modernisiert

---

## [3.0.0] – 2025-06-28
### Major Features & Breaking Changes
- **Modulsystem:**
  - Import/Export von Funktionen und Variablen mit `HOLE ... VON ...` und `GIBFREI ...` (inkl. Export-Listen)
  - Importiert werden können nur explizit exportierte Namen
  - Reihenfolge der Statements im Modul beliebig
- **Exit-Code-Konvention:**
  - Die Funktion `haupt` muss immer `GANZ` (int) als Rückgabetyp haben und einen Exit-Code zurückgeben (`ZURÜCK 0;`)
  - Programme ohne oder mit falschem `haupt` liefern eine klare Fehlermeldung
- **Fehlerbehandlung:**
  - Try/Catch-Mechanik (`VERSUCHE`/`FANGE`) für robustere Programme
- **Methoden für KISTE und WORT:**
  - `.LÄNGE`, `.HINZUFÜGEN`, `.ERWEITERN` für Listen/Strings
- **Mehrdimensionale Arrays:**
  - Arrays können Arrays enthalten, Zuweisung an beliebige Array-Elemente
- **Parser/Interpreter:**
  - AST und Ausführung für Methoden, Properties, SetExpression, Modulsystem
  - Verbesserte Fehlermeldungen, Exit-Code-Prüfung
- **Dokumentation:**
  - Alle relevanten Doku-Dateien und Beispiele auf neuen Stand gebracht

### Hinweise
- Diese Version ist nicht abwärtskompatibel zu 2.x (insbesondere wegen `GANZ haupt()`-Pflicht und Modulsystem)
- Siehe `docs/modulsystem.md`, `docs/BEISPIELE.md`, `docs/funktionen.md` für Details und Beispiele

---

## [2.0.0] – 2025-06-28
### Breaking Changes & Major Features
- **Methoden für Datentypen:**
  - Listen (KISTE): `.LÄNGE`, `.HINZUFÜGEN(wert)`, `.ERWEITERN(wert)`
  - Strings (WORT): `.LÄNGE`
- **Mehrdimensionale Arrays:**
  - Arrays können Arrays enthalten, z.B. `KISTE matrix = [[1,2],[3,4]];`
  - Zuweisung und Zugriff auf beliebige Array-Elemente möglich: `matrix[0][1] = 99;`
- **Zuweisung an beliebige Ausdrücke:**
  - Zuweisung an Array-Elemente, Properties und komplexe Ausdrücke unterstützt
- **Parser und Interpreter:**
  - AST und Ausführung für Methoden-Dispatch, Property-Access, SetExpression
- **Dokumentation:**
  - Alle relevanten Doku-Dateien und Beispiele auf neuen Stand gebracht

### Hinweise
- Diese Version ist nicht vollständig abwärtskompatibel zu 1.x.
- Siehe `docs/arrays.md`, `docs/variablen.md`, `docs/BEISPIELE.md`, `docs/SPRACHE.md` für Details und Beispiele.

---

## [1.1.0] – ...
*Frühere Änderungen siehe ältere Releases*
