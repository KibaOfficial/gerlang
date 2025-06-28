# GerLang – Variablen

## Deklaration
- Variablen werden immer mit Typ deklariert.
- Syntax: `TYP name = wert;`
- Arrays (KISTE) und mehrdimensionale Arrays sind möglich.
- Zuweisungen an Array-Elemente und Properties werden unterstützt.

Beispiel:
```gerlang
GANZ zahl = 5;
KOMMA pi = 3.14;
WORT name = "Max";
JAIN wahr = JA;
KISTE zahlen = [1, 2, 3];
KISTE matrix = [[1,2],[3,4]];
```

## Zuweisung
- Variablen können neu zugewiesen werden:
```gerlang
zahl = 7;
```
- Auch Array-Elemente und Properties:
```gerlang
zahlen[1] = 99;
matrix[0][1] = 42;
```

## Methoden für Variablen/Datentypen
- Strings (WORT) und Arrays (KISTE) unterstützen Methoden:
  - `wort.LÄNGE` – Länge des Strings
  - `kiste.LÄNGE` – Anzahl der Elemente
  - `kiste.HINZUFÜGEN(wert)` – Fügt am Anfang ein
  - `kiste.ERWEITERN(wert)` – Fügt am Ende an

Beispiel:
```gerlang
WORT text = "Hallo";
GANZ n = text.LÄNGE; // n = 5
zahlen.ERWEITERN(4); // zahlen = [1,2,3,4]
```

## Sichtbarkeit & Gültigkeitsbereich
- Variablen sind innerhalb des Blocks sichtbar, in dem sie deklariert wurden.
- Es gibt keine globalen Variablen außerhalb von Funktionen.

## Namensgebung
- Namen sollten beschreibend und klein geschrieben sein.
- Keine Sonderzeichen außer `_` erlaubt.

## Initialisierung
- Variablen müssen bei der Deklaration initialisiert werden.

---

Weitere Hinweise zu Variablen findest du in den Beispielen und im FAQ.
