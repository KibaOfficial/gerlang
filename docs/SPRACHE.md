# GerLang – Sprachreferenz

> **GerLang** ist eine moderne, deutschsprachige Programmiersprache mit TypeScript-Style Fehlermeldungen und professioneller Entwicklererfahrung.

---

## 📋 Inhaltsverzeichnis
1. [Einleitung](#1-einleitung)
2. [Grundlegende Syntax](#2-grundlegende-syntax)
3. [Datentypen](#3-datentypen)
4. [Variablen & Zuweisung](#4-variablen--zuweisung)
5. [Operatoren](#5-operatoren)
6. [Kontrollstrukturen](#6-kontrollstrukturen)
7. [Funktionen & Rückgabewerte](#7-funktionen--rückgabewerte)
8. [Arrays (KISTE)](#8-arrays-kiste)
9. [Methoden für Datentypen](#9-methoden-für-datentypen)
10. [Modulsystem](#10-modulsystem)
11. [Fehlerbehandlung](#11-fehlerbehandlung)
12. [Ein-/Ausgabe](#12-ein-ausgabe)
13. [Beispielprogramme](#13-beispielprogramme)

---

## 1. Einleitung

GerLang ist eine **deutschsprachige, C-ähnliche Programmiersprache** mit moderner, klarer Syntax. Ziel ist es, Programmierkonzepte auf Deutsch zugänglich zu machen und dabei **Turing-Vollständigkeit** sowie moderne Sprachfeatures zu bieten.

### ✨ Hauptfeatures
- 🇩🇪 **Vollständig deutschsprachige Syntax**
- 🔧 **TypeScript-Style Fehlermeldungen** mit präzisen Positionen
- 📦 **Modulsystem** mit Import/Export
- 🛡️ **Robuste Fehlerbehandlung** (try/catch)
- 🔢 **Mehrdimensionale Arrays** und Methoden
- 🚀 **Professionelle Entwicklererfahrung**

---

## 2. Grundlegende Syntax

### Anweisungen & Struktur
- **Anweisungen** enden mit Semikolon (`;`)
- **Blöcke** werden mit `{ ... }` geklammert
- **Kommentare:** `// Kommentar` oder `HINWEIS: Kommentar`

```gerlang
// Einzeiliger Kommentar
HINWEIS: Auch ein Kommentar

GANZ x = 5;        // Anweisung mit Semikolon
{                  // Block-Anfang
    DRUCKE(x);
}                  // Block-Ende
```

### Hauptfunktion
Jedes GerLang-Programm benötigt eine `haupt()`-Funktion:

```gerlang
GANZ haupt() {
    DRUCKE("Hallo, Welt!");
    ZURÜCK 0;  // Exit-Code
}
```

---

## 3. Datentypen

| Typ     | Bedeutung             | Beispiel                    | Literale           |
|---------|----------------------|----------------------------|-------------------|
| `GANZ`  | Ganzzahl (int)       | `GANZ x = 5;`              | `42`, `-17`, `0`  |
| `KOMMA` | Kommazahl (float)    | `KOMMA pi = 3.14;`         | `3.14`, `-0.5`    |
| `WORT`  | Zeichenkette (str)   | `WORT name = "Max";`       | `"Hallo"`, `""`   |
| `JAIN`  | Boolescher Wert      | `JAIN ok = JA;`            | `JA`, `NEIN`      |
| `KISTE` | Array/Liste          | `KISTE zahlen = [1,2,3];`  | `[1,2,3]`, `[]`   |

### Besondere Werte
- **Boolesche Literale:** `JA` (true), `NEIN` (false)
- **Arrays** sind nullbasiert und können beliebige Typen enthalten

### String-Interpolation (Template-Strings)
GerLang unterstützt moderne String-Interpolation mit `${...}` Syntax:

```gerlang
WORT name = "Anna";
GANZ alter = 25;
KISTE hobbys = ["Lesen", "Sport", "Musik"];

// Einfache Variablen
DRUCKE("Hallo ${name}!");  // "Hallo Anna!"

// Komplexe Ausdrücke
DRUCKE("${name} ist ${alter} Jahre alt und wird nächstes Jahr ${alter + 1}");

// Methoden-Aufrufe
DRUCKE("${name} hat ${hobbys.LÄNGE} Hobbys");

// Arithmetische Operationen
DRUCKE("2 + 3 = ${2 + 3}");  // "2 + 3 = 5"
```

**Vorteile:**
- Keine String-Concatenation mit `+` nötig
- Lesbarerer Code für komplexe String-Formatierung
- Direkte Ausführung von Ausdrücken im String

---

## 4. Variablen & Zuweisung

### Deklaration mit Initialisierung
```gerlang
GANZ zahl = 5;
KOMMA pi = 3.14;
WORT name = "Max Mustermann";
JAIN aktiv = JA;
KISTE zahlen = [1, 2, 3, 4, 5];
KISTE matrix = [[1,2], [3,4]];  // Mehrdimensional
```

### Zuweisungen
```gerlang
// Einfache Zuweisung
zahl = 10;

// Array-Element Zuweisung
zahlen[0] = 99;
matrix[1][0] = 42;

// Methodenaufrufe (siehe unten)
zahlen.ERWEITERN(6);
```

---

## 5. Operatoren

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
- `UND` Logisches Und (`&&`)
- `ODER` Logisches Oder (`||`)
- `NICHT` Logisches Nicht (`!`)

### Zugriff & Methoden  
- `kiste[index]` Array-Zugriff
- `objekt.METHODE(...)` Methodenaufruf
- `objekt.EIGENSCHAFT` Property-Zugriff

### Beispiel mit komplexen Ausdrücken
```gerlang
WENN ((a > 0 UND b > 0) ODER (a == b)) {
    DRUCKE("Bedingung erfüllt");
}
```

---

## 6. Kontrollstrukturen

### Bedingungen
```gerlang
WENN (bedingung) {
    // Anweisungen wenn wahr
} SONST {
    // Anweisungen wenn falsch
}

// Verschachtelt möglich
WENN (x > 10) {
    DRUCKE("Groß");
} SONST WENN (x > 5) {
    DRUCKE("Mittel");
} SONST {
    DRUCKE("Klein");
}
```

### Schleifen
```gerlang
// While-Schleife
SOLANGE (bedingung) {
    // Wiederholt solange bedingung wahr ist
}

// For-Schleife
FÜR (GANZ i = 0; i < zahlen.LÄNGE; i = i + 1) {
    DRUCKE("Element " + i + ": " + zahlen[i]);
}
```

---

## 7. Funktionen & Rückgabewerte

### Funktionsdefinition
```gerlang
RÜCKGABETYP funktionsname(parameter1: TYP, parameter2: TYP) {
    // Funktionskörper
    ZURÜCK wert;
}
```

### Beispiele
```gerlang
// Funktion mit Rückgabewert
GANZ addiere(a: GANZ, b: GANZ) {
    ZURÜCK a + b;
}

// Funktion ohne Rückgabewert
NIX begrüße(name: WORT) {
    DRUCKE("Hallo, " + name + "!");
}

// Rekursive Funktion
GANZ fakultät(n: GANZ) {
    WENN (n <= 1) {
        ZURÜCK 1;
    }
    ZURÜCK n * fakultät(n - 1);
}
```

---

## 8. Arrays (KISTE)

### Grundlagen
```gerlang
// Array-Deklaration
KISTE zahlen = [1, 2, 3, 4, 5];
KISTE gemischt = [1, "zwei", 3.14, JA];

// Zugriff (nullbasiert)
GANZ erstes = zahlen[0];        // 1
GANZ letztes = zahlen[4];       // 5
```

### Mehrdimensionale Arrays
```gerlang
// 2D-Array (Matrix)
KISTE matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];

// Zugriff auf 2D-Elemente
GANZ wert = matrix[1][2];  // 6
matrix[0][0] = 99;         // Zuweisung
```

### Array-Iteration
```gerlang
KISTE namen = ["Alice", "Bob", "Charlie"];

FÜR (GANZ i = 0; i < namen.LÄNGE; i = i + 1) {
    DRUCKE("Name " + i + ": " + namen[i]);
}
```

---

## 9. Methoden für Datentypen

### String-Methoden (WORT)
```gerlang
WORT text = "Hallo Welt";
GANZ länge = text.LÄNGE;        // 10
```

### Array-Methoden (KISTE)
```gerlang
KISTE liste = [1, 2, 3];

// Eigenschaften
GANZ anzahl = liste.LÄNGE;      // 3

// Methoden zum Hinzufügen
liste.HINZUFÜGEN(0);            // Am Anfang: [0, 1, 2, 3]
liste.ERWEITERN(4);             // Am Ende: [0, 1, 2, 3, 4]

DRUCKE("Neue Länge: " + liste.LÄNGE);  // 5
```

---

## 10. Modulsystem

### Exportieren (GIBFREI)
```gerlang
// math.gerl - Mathematik-Modul

// Direkt-Export bei Definition
GIBFREI GANZ addiere(a: GANZ, b: GANZ) {
    ZURÜCK a + b;
}

GIBFREI GANZ PI = 3.14159;

// Oder nachträgliche Export-Liste
GANZ multipliziere(a: GANZ, b: GANZ) {
    ZURÜCK a * b;
}

GIBFREI multipliziere;  // Nachträglich exportiert
```

### Importieren (HOLE ... VON)
```gerlang
// main.gerl - Hauptprogramm
HOLE addiere, PI, multipliziere VON "math.gerl";

GANZ haupt() {
    GANZ summe = addiere(5, 3);          // 8
    GANZ produkt = multipliziere(4, 7);  // 28
    DRUCKE("Summe: " + summe);
    DRUCKE("Produkt: " + produkt);
    DRUCKE("PI: " + PI);
    ZURÜCK 0;
}
```

---

## 11. Fehlerbehandlung

### Try-Catch (VERSUCHE/FANGE)
```gerlang
GANZ sichere_division(a: GANZ, b: GANZ) {
    VERSUCHE() {
        ZURÜCK a / b;
    } FANGE fehler {
        DRUCKE("Fehler abgefangen: " + fehler);
        ZURÜCK 0;
    }
}

GANZ haupt() {
    GANZ result = sichere_division(10, 0);  // Keine Programmunterbrechung
    DRUCKE("Ergebnis: " + result);
    ZURÜCK 0;
}
```

### Erweiterte Fehlerbehandlung
GerLang bietet **TypeScript-Style Fehlermeldungen** mit:
- 🎯 **Präzise Positionsangaben** (Zeile:Spalte)
- 🎨 **Farbige Ausgabe** mit Kontext
- 📋 **Error-Codes** (GL001, GL002, etc.)
- 💡 **Hilfreiche Tipps** für häufige Fehler
- 📚 **Call-Stack** bei Runtime-Fehlern

---

## 12. Ein-/Ausgabe

### Ausgabe
```gerlang
DRUCKE("Einfacher Text");
DRUCKE(variable);
DRUCKE("Wert: " + variable);
```

### Eingabe 
```gerlang
WORT eingabe = LESE("Bitte Namen eingeben: ");
DRUCKE("Hallo, " + eingabe + "!");
```

### Built-in Funktionen

#### 🔢 Mathematische Funktionen
```gerlang
// Grundrechenarten
KOMMA wurzel = WURZEL(16);          // 4.0
KOMMA potenz = POTENZ(2, 3);        // 8.0 (2^3)
KOMMA betrag = ABS(-5);             // 5.0

// Rundung
GANZ gerundet = RUNDEN(3.7);        // 4
KOMMA genau = RUNDEN(3.14159, 2);   // 3.14

// Zufallszahlen
KOMMA zufall = ZUFALLSZAHL();           // 0.0 - 1.0
GANZ würfel = ZUFALLSBEREICH(1, 6);     // 1-6
```

#### 🔄 Typ-Konvertierung
```gerlang
// String-Konvertierung
WORT text1 = ZU_WORT(42);         // "42"
WORT text2 = ZU_WORT(3.14);       // "3.14"

// Zahlen-Konvertierung  
GANZ zahl1 = ZU_GANZ("42");       // 42
GANZ zahl2 = ZU_GANZ(3.7);        // 3
KOMMA komma = ZU_KOMMA("3.14");   // 3.14

// Alternative Syntax (auch verfügbar):
WORT text = WORT(42);             // "42"
GANZ zahl = GANZ("42");           // 42
KOMMA float = KOMMA("3.14");      // 3.14
```

---

## 13. Beispielprogramme

### Komplettes Programm: Zahlenraten
```gerlang
GANZ haupt() {
    GANZ geheimzahl = ZUFALLSBEREICH(1, 100);  // Neue Math-Funktion!
    GANZ versuche = 0;
    GANZ geraten = 0;
    
    DRUCKE("=== Zahlenraten-Spiel ===");
    DRUCKE("Ich denke an eine Zahl zwischen 1 und 100!");
    
    SOLANGE (geraten != geheimzahl) {
        WORT eingabe = LESE("Dein Tipp: ");
        
        VERSUCHE() {
            geraten = ZU_GANZ(eingabe);  // Typ-Konvertierung
            versuche = versuche + 1;
            
            WENN (geraten < geheimzahl) {
                DRUCKE("Zu niedrig!");
            } SONST WENN (geraten > geheimzahl) {
                DRUCKE("Zu hoch!");
            } SONST {
                DRUCKE("🎉 Richtig! Du hast " + versuche + " Versuche gebraucht.");
            }
        } FANGE fehler {
            DRUCKE("Bitte eine gültige Zahl eingeben!");
        }
    }
    
    ZURÜCK 0;
}
```

---

## 📚 Weitere Dokumentation

- 📖 [Detaillierte Beispiele](BEISPIELE.md)
- 🔧 [Funktionen & Parameter](funktionen.md)
- 📊 [Arrays & Datenstrukturen](arrays.md)
- 🚨 [Fehlerbehandlung](fehlerbehandlung.md)
- 📦 [Modulsystem](modulsystem.md)
- ❓ [FAQ & Troubleshooting](faq.md)

---

**GerLang** – Programmieren auf Deutsch, professionell und modern! 🚀

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
