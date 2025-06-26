# GerLang – Ausführliche Sprachdokumentation

## Einleitung
GerLang ist eine deutschsprachige, C-ähnliche Programmiersprache mit moderner, klarer Syntax. Ziel ist es, Programmierkonzepte auf Deutsch zugänglich zu machen und dabei Turing-Vollständigkeit sowie moderne Sprachfeatures zu bieten.

---

## Inhaltsverzeichnis
1. Grundlegende Syntax
2. Datentypen
3. Variablen & Zuweisung
4. Operatoren
5. Kontrollstrukturen
6. Funktionen & Rückgabewerte
7. Arrays (KISTE)
8. Ein-/Ausgabe
9. Fehlerbehandlung
10. Besonderheiten & Hinweise
11. FAQ

---

## 1. Grundlegende Syntax
- **Anweisungen** enden mit Semikolon (`;`).
- **Blöcke** werden mit `{ ... }` geklammert.
- **Kommentare:** `// Kommentar` oder `HINWEIS: Kommentar`

Beispiel:
```gerlang
// Einzeiliger Kommentar
HINWEIS: Auch ein Kommentar
GANZ x = 5;
```

---

## 2. Datentypen
| Typ   | Bedeutung           | Beispiel         |
|-------|---------------------|-----------------|
| GANZ  | Ganzzahl (int)      | GANZ x = 5;     |
| KOMMA | Kommazahl (float)   | KOMMA pi = 3.14;|
| WORT  | Zeichenkette (str)  | WORT name = "Max";|
| JAIN  | Boolescher Wert     | JAIN ok = JA;   |
| KISTE | Array/Liste         | KISTE zahlen = [1,2,3];|

- **Boolesche Literale:** `JA`, `NEIN`, `VIELLEICHT` (None/Null)
- **Arrays** sind nullbasiert und können beliebige Typen enthalten.

---

## 3. Variablen & Zuweisung
Variablen werden mit Typ deklariert und können überall im Code stehen.
```gerlang
GANZ zahl = 5;
KOMMA pi = 3.14;
WORT name = "Max";
JAIN wahr = JA;
KISTE zahlen = [1, 2, 3];
```

---

## 4. Operatoren
- **Arithmetisch:** `+`, `-`, `*`, `/`, `%`
- **Vergleich:** `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Logisch:** `UND`, `ODER`, `NICHT`
- **Array-Zugriff:** `kiste[index]`

Beispiel:
```gerlang
WENN (a > 0 UND b > 0) ODER (a == b) {
  DRUCKE("Bedingung erfüllt");
}
```

---

## 5. Kontrollstrukturen
### Bedingung
```gerlang
WENN (Bedingung) {
  // ...
} SONST {
  // ...
}
```
### Schleifen
```gerlang
SOLANGE (Bedingung) {
  // ...
}
FÜR (GANZ i = 0; i < 10; i = i + 1) {
  // ...
}
```

---

## 6. Funktionen & Rückgabewerte
- Parameter mit Typ: `name: TYP`
- Rückgabewert mit `ZURÜCK`.
- Rekursion wird unterstützt.

Beispiel:
```gerlang
GANZ addiere(a: GANZ, b: GANZ) {
  ZURÜCK a + b;
}
NIX haupt() {
  DRUCKE(addiere(2, 3));
  ZURÜCK 0;
}
```

---

## 7. Arrays (KISTE)
- Arrays sind nullbasiert.
- Zugriff: `kiste[index]`
- Arrays können beliebige Typen enthalten.

Beispiel:
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

---

## 8. Ein-/Ausgabe
- `DRUCKE(...)` gibt Werte aus.
- `LESE()` liest Benutzereingabe (bald verfügbar).

Beispiel:
```gerlang
DRUCKE("Text");
// GANZ eingabe = LESE();
```

---

## 9. Fehlerbehandlung
- Fehlerbehandlung (`VERSUCHE`/`FANGE`) ist geplant, aber noch nicht implementiert.

---

## 10. Besonderheiten & Hinweise
- Alle Schlüsselwörter sind deutsch.
- Typisierung ist strikt.
- Arrays (KISTE) können beliebige Typen enthalten.
- Siehe Beispielprogramme im `examples/`-Verzeichnis.

---

## 11. FAQ
**Frage:** Kann ich eigene Datentypen definieren?
> Noch nicht, aber geplant (siehe `ORDNUNG`/`DING`).

**Frage:** Gibt es eine Standardbibliothek?
> Nein, aber einige eingebaute Funktionen wie `DRUCKE`, `LESE`, Typumwandlungen.

**Frage:** Wie kann ich Fehler abfangen?
> Fehlerbehandlung ist geplant, aktuell werden Fehler als Ausnahmen angezeigt.

**Frage:** Wie kann ich Programme ausführen?
> Siehe README und CLI-Befehle.
