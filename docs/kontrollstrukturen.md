# GerLang – Kontrollstrukturen

## Bedingungen
- `WENN (Bedingung) { ... } SONST { ... }`
- Mehrere verschachtelte Bedingungen möglich.

Beispiel:
```gerlang
WENN (x > 0) {
  DRUCKE("Positiv");
} SONST {
  DRUCKE("Nicht positiv");
}
```

## Schleifen
- `SOLANGE (Bedingung) { ... }` (while)
- `FÜR (GANZ i = 0; i < 10; i = i + 1) { ... }` (for)

Beispiel:
```gerlang
SOLANGE (x < 10) {
  x = x + 1;
}
FÜR (GANZ i = 0; i < 5; i = i + 1) {
  DRUCKE(i);
}
```

## Fehlerquellen
- Klammern und Semikolons nicht vergessen!
- Bedingungen müssen einen booleschen Wert liefern.

---

Weitere Beispiele findest du in den Beispielprogrammen.
