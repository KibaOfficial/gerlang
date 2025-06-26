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
9. Ein-/Ausgabe
10. Fehlerbehandlung
11. Beispiele
12. Besonderheiten & Hinweise

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
```

Variablen können überall im Code deklariert werden. Typen sind verpflichtend.

---

## 5. Operatoren
- Arithmetisch: `+`, `-`, `*`, `/`, `%`
- Vergleich: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Logisch: `UND`, `ODER`, `NICHT`
- Array-Zugriff: `kiste[index]`

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

FÜR (GANZ i = 0; i < 10; i = i + 1) {
  // ...
}
```

---

## 7. Funktionen & Rückgabewerte
```gerlang
GANZ addiere(a: GANZ, b: GANZ) {
  ZURÜCK a + b;
}

NIX haupt() {
  DRUCKE(addiere(2, 3));
  ZURÜCK 0;
}
```
- Parameter mit Typ: `name: TYP`
- Rückgabewert mit `ZURÜCK`.
- Rekursion wird unterstützt.

---

## 8. Arrays (KISTE)
```gerlang
KISTE jahre = [2000, 2001, 2002, 2003];
FÜR (GANZ i = 0; i < 4; i = i + 1) {
  GANZ jahr = jahre[i];
  WENN (jahr == 2003) {
    DRUCKE(jahr + " Hier bin ich geboren");
  } SONST {
    DRUCKE(jahr);
  }
}
```
- Arrays sind nullbasiert.
- Zugriff: `kiste[index]`

---

## 9. Ein-/Ausgabe
```gerlang
DRUCKE("Text");
// LESE() für Benutzereingabe (in Entwicklung)
```
- `DRUCKE(...)` gibt Werte aus.
- `LESE()` liest Benutzereingabe (bald verfügbar).

---

## 10. Fehlerbehandlung
- Fehlerbehandlung (z.B. `VERSUCHE`/`FANGE`) ist geplant, aber noch nicht implementiert.

---

## 11. Beispiele
```gerlang
GANZ fakultaet(n: GANZ) {
  WENN (n < 2) {
    ZURÜCK 1;
  }
  ZURÜCK n * fakultaet(n-1);
}

NIX haupt() {
  DRUCKE(fakultaet(5));
  ZURÜCK 0;
}
```

---

## 12. Besonderheiten & Hinweise
- Alle Schlüsselwörter sind deutsch.
- Typisierung ist strikt.
- Arrays (KISTE) können beliebige Typen enthalten.
- Siehe Beispielprogramme im `examples/`-Verzeichnis.

---

Weitere Infos und aktuelle Beispiele findest du in den Beispiel-Dateien und der README.
