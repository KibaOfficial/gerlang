# GerLang – Operatoren

## Übersicht
GerLang unterstützt verschiedene Operatoren für mathematische, logische und Vergleichsoperationen.

### Arithmetische Operatoren
- `+` Addition
- `-` Subtraktion
- `*` Multiplikation
- `/` Division
- `%` Modulo

### Vergleichsoperatoren
- `==` Gleichheit
- `!=` Ungleichheit
- `<`, `>`, `<=`, `>=` Größenvergleiche

### Logische Operatoren
- `UND` Logisches Und
- `ODER` Logisches Oder
- `NICHT` Logisches Nicht

### Array-Zugriff
- `kiste[index]` Zugriff auf Array-Element

## Operator-Priorität
- Klammern `()` können genutzt werden, um die Reihenfolge zu steuern.

Beispiel:
```gerlang
WENN ((a > 0 UND b > 0) ODER (a == b)) {
  DRUCKE("Bedingung erfüllt");
}
```

---

Weitere Operatoren und Beispiele findest du in den Kapiteln zu Kontrollstrukturen und Arrays.
