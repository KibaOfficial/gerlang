# GerLang – Fehlerbehandlung

## Aktueller Stand
- Fehlerbehandlung mit `VERSUCHE`/`FANGE` ist jetzt implementiert!
- Fehler können im Code abgefangen und behandelt werden, das Programm läuft danach weiter.

## Syntax
```gerlang
VERSUCHE() {
  // Code, der fehlschlagen könnte
} FANGE fehler {
  DRUCKE("Fehler: " + fehler);
}
```

## Beispiel
```gerlang
NIX beispiel() {
  VERSUCHE() {
    GANZ x = 5 / 0;
  } FANGE fehler {
    DRUCKE("Fehler abgefangen: " + fehler);
  }
}
```

## Tipps
- Fehler können als Variable im FANGE-Block verwendet werden.
- Nutze Fehlerbehandlung für robustere Programme und besseres Debugging.

---

Weitere Hinweise findest du in der FAQ.
