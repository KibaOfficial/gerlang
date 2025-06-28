# GerLang – Sprachreferenz

## Inhaltsverzeichnis
1. Einleitung
2. Grundlegende Syntax
3. Datentypen
4. Variablen & Zuweisung
5. Operatoren
6. Kontrollstrukturen
7. Funktionen & Rückgabewerte
8. Arrays (KISTE)
9. Methoden für Datentypen
10. Mehrdimensionale Arrays
11. Ein-/Ausgabe
12. Fehlerbehandlung
13. Beispiele
14. Besonderheiten & Hinweise

---

## 1. Einleitung
GerLang ist eine deutschsprachige, C-ähnliche Programmiersprache mit moderner, klarer Syntax. Ziel ist es, Programmierkonzepte auf Deutsch zugänglich zu machen und dabei Turing-Vollständigkeit sowie moderne Sprachfeatures zu bieten.

---

## 2. Grundlegende Syntax
- Anweisungen enden mit Semikolon (`;`).
- Blöcke werden mit `{ ... }` geklammert.
- Kommentare: `// Kommentar` oder `HINWEIS: Kommentar`

```gerlang
// Einzeiliger Kommentar
HINWEIS: Auch ein Kommentar
```

---

## 3. Datentypen
| Typ   | Bedeutung           | Beispiel         |
|-------|---------------------|-----------------|
| GANZ  | Ganzzahl (int)      | GANZ x = 5;     |
| KOMMA | Kommazahl (float)   | KOMMA pi = 3.14;|
| WORT  | Zeichenkette (str)  | WORT name = "Max";|
| JAIN  | Boolescher Wert     | JAIN ok = JA;   |
| KISTE | Array/Liste         | KISTE zahlen = [1,2,3];|

---

## 4. Variablen & Zuweisung
```gerlang
GANZ zahl = 5;
KOMMA pi = 3.14;
WORT name = "Max";
JAIN wahr = JA;
KISTE zahlen = [1, 2, 3];
KISTE matrix = [[1,2],[3,4]];
```

- Zuweisung an Array-Elemente: `zahlen[1] = 42;`
- Zuweisung an mehrdimensionale Arrays: `matrix[0][1] = 99;`

---

## 5. Operatoren
- Arithmetisch: `+`, `-`, `*`, `/`, `%`
- Vergleich: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Logisch: `UND`, `ODER`, `NICHT`
- Array-Zugriff: `kiste[index]`
- Methoden- und Property-Zugriff: `objekt.METHODE(...)`, `objekt.PROPERTY`

---

## 6. Kontrollstrukturen
```gerlang
WENN (Bedingung) {
  // ...
} SONST {
  // ...
}

SOLANGE (Bedingung) {
  // ...
}

FÜR (GANZ i = 0; i < zahlen.LÄNGE; i = i + 1) {
  DRUCKE(zahlen[i]);
}
```

---

## 7. Funktionen & Rückgabewerte
```gerlang
GANZ add(a: GANZ, b: GANZ) {
  ZURÜCK a + b;
}
```

---

## 8. Arrays (KISTE)
- Arrays werden mit `KISTE` deklariert.
- Mehrdimensionale Arrays sind möglich: `KISTE matrix = [[1,2],[3,4]];`
- Zugriff: `kiste[index]`, `matrix[1][0]`
- Methoden: siehe unten

---

## 9. Methoden für Datentypen
- Für Strings (WORT):
  - `wort.LÄNGE` – Länge des Strings
- Für Arrays (KISTE):
  - `kiste.LÄNGE` – Anzahl der Elemente
  - `kiste.HINZUFÜGEN(wert)` – Fügt am Anfang ein
  - `kiste.ERWEITERN(wert)` – Fügt am Ende an

Beispiel:
```gerlang
KISTE liste = [1,2];
liste.HINZUFÜGEN(0); // [0,1,2]
liste.ERWEITERN(3);  // [0,1,2,3]
GANZ n = liste.LÄNGE; // n = 4
WORT text = "Hallo";
GANZ l = text.LÄNGE; // l = 5
```

---

## 10. Mehrdimensionale Arrays
- Arrays können Arrays enthalten:
```gerlang
KISTE matrix = [[1,2],[3,4]];
matrix[0][1] = 99;
```

---

## 11. Ein-/Ausgabe
- `DRUCKE(...)` oder `ZEIGE(...)` für Ausgabe
- `LESE()` für Benutzereingabe

---

## 12. Fehlerbehandlung
- Mit `VERSUCHE { ... } FANGE { ... }` können Fehler abgefangen werden.

---

## 13. Beispiele
Siehe `BEISPIELE.md` und die Beispielprogramme im Ordner `examples/`.

---

## 14. Besonderheiten & Hinweise
- Methoden und Properties für Datentypen
- Zuweisung an beliebige Ausdrücke (z.B. Array-Elemente)
- Mehrdimensionale Arrays
- Moderne, deutschsprachige Syntax

---

Weitere Infos und aktuelle Beispiele findest du in den Beispiel-Dateien und der README.
