# GerLang – Arrays (KISTE)

## Definition
- Arrays werden mit `KISTE` deklariert.
- Syntax: `KISTE name = [wert1, wert2, ...];`

Beispiel:
```gerlang
KISTE zahlen = [1, 2, 3];
KISTE gemischt = [1, "zwei", 3.0];
```

## Zugriff
- Zugriff über Index: `kiste[index]`
- Indizes beginnen bei 0.

Beispiel:
```gerlang
GANZ erstes = zahlen[0];
```

## Iteration
- Mit Schleifen über Arrays iterieren:
```gerlang
FÜR (GANZ i = 0; i < 3; i = i + 1) {
  DRUCKE(zahlen[i]);
}
```

## Besonderheiten
- Arrays können beliebige Typen enthalten.

---

Weitere Beispiele findest du in den Beispielprogrammen.
