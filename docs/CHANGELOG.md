# Changelog für GerLang

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
