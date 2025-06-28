# Changelog für GerLang

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
