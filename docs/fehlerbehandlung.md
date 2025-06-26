# GerLang – Fehlerbehandlung

## Aktueller Stand
- Fehlerbehandlung mit `VERSUCHE`/`FANGE` ist geplant, aber noch nicht implementiert.
- Fehler werden aktuell als Ausnahmen angezeigt und beenden das Programm.

## Geplante Syntax
```gerlang
VERSUCHE {
  // Code, der fehlschlagen könnte
} FANGE (fehler) {
  DRUCKE("Fehler: " + fehler);
}
```

## Tipps
- Code gut testen, um Fehler früh zu erkennen.
- Kommentare nutzen, um auf mögliche Fehlerquellen hinzuweisen.

---

Weitere Hinweise findest du in der FAQ.
