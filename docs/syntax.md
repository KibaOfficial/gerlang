# GerLang – Syntax

## Einleitung
Hier findest du eine ausführliche Beschreibung der grundlegenden Syntaxregeln von GerLang, inklusive Formatierung, Kommentare, Namenskonventionen und Best Practices.

---

## Anweisungen
- Jede Anweisung endet mit einem Semikolon (`;`).
- Mehrere Anweisungen können in einem Block `{ ... }` zusammengefasst werden.

## Kommentare
- Einzeilige Kommentare: `// Kommentartext`
- Alternative: `HINWEIS: Kommentartext`
- Kommentare werden vom Interpreter ignoriert.

## Blöcke
- Blöcke werden mit geschweiften Klammern `{ ... }` definiert.
- Beispiel:

```gerlang
WENN (Bedingung) {
  // Block mit mehreren Anweisungen
  GANZ x = 5;
  DRUCKE(x);
}
```

## Namenskonventionen
- Variablen- und Funktionsnamen sollten beschreibend und klein geschrieben werden (z.B. `anzahl`, `berechne_summe`).
- Keine Sonderzeichen außer `_` erlaubt.

## Best Practices
- Kommentare nutzen, um Code verständlich zu machen.
- Blöcke und Einrückungen übersichtlich gestalten.
- Aussagekräftige Namen verwenden.

---

Weitere Beispiele und Hinweise findest du in den anderen Dokumentationsdateien.
