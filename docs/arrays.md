# GerLang – Arrays (KISTE)

## Definition
- Arrays werden mit `KISTE` deklariert.
- Syntax: `KISTE name = [wert1, wert2, ...];`
- Mehrdimensionale Arrays sind möglich: `KISTE matrix = [[1,2],[3,4]];`

Beispiel:
```gerlang
KISTE zahlen = [1, 2, 3];
KISTE gemischt = [1, "zwei", 3.0];
KISTE matrix = [[1,2],[3,4]];
```

## Zugriff
- Zugriff über Index: `kiste[index]`
- Indizes beginnen bei 0.
- Mehrdimensional: `matrix[1][0]` (ergibt 3)

Beispiel:
```gerlang
GANZ erstes = zahlen[0];
GANZ wert = matrix[1][0]; // ergibt 3
```

## Zuweisung an Array-Elemente
- Einzelne Elemente können direkt zugewiesen werden:
```gerlang
zahlen[2] = 42;
matrix[0][1] = 99;
```

## Methoden für Arrays (KISTE)
- `kiste.LÄNGE` – Gibt die Anzahl der Elemente zurück
- `kiste.HINZUFÜGEN(wert)` – Fügt ein Element am Anfang ein
- `kiste.ERWEITERN(wert)` – Fügt ein Element am Ende an

Beispiele:
```gerlang
KISTE liste = [1,2];
liste.HINZUFÜGEN(0); // liste = [0,1,2]
liste.ERWEITERN(3);  // liste = [0,1,2,3]
GANZ n = liste.LÄNGE; // n = 4
```

## Iteration
- Mit Schleifen über Arrays iterieren:
```gerlang
FÜR (GANZ i = 0; i < zahlen.LÄNGE; i = i + 1) {
  DRUCKE(zahlen[i]);
}
```

## Besonderheiten
- Arrays können beliebige Typen enthalten.
- Mehrdimensionale Arrays werden wie verschachtelte Listen behandelt.
- Methoden und Zuweisungen an Array-Elemente werden wie oben beschrieben unterstützt.

---

Weitere Beispiele findest du in den Beispielprogrammen und in der Datei `BEISPIELE.md`.
