# 🔢 GerLang – Operatoren-Referenz

> **Vollständige Operatoren-Referenz** für GerLang mit Prioritäten, Beispielen und fortgeschrittenen Features.

---

## 📋 Inhaltsverzeichnis
1. [Arithmetische Operatoren](#-arithmetische-operatoren)
2. [Vergleichsoperatoren](#-vergleichsoperatoren)
3. [Logische Operatoren](#-logische-operatoren)
4. [Zugriffs-Operatoren](#-zugriffs-operatoren)
5. [Operator-Priorität](#-operator-priorität)
6. [Erweiterte Beispiele](#-erweiterte-beispiele)

---

## ➕ Arithmetische Operatoren

### Grundoperationen
| Operator | Bedeutung      | Beispiel           | Ergebnis |
|----------|---------------|-------------------|----------|
| `+`      | Addition      | `5 + 3`           | `8`      |
| `-`      | Subtraktion   | `10 - 4`          | `6`      |
| `*`      | Multiplikation| `3 * 7`           | `21`     |
| `/`      | Division      | `15 / 3`          | `5`      |
| `%`      | Modulo        | `17 % 5`          | `2`      |

### Beispiele mit verschiedenen Datentypen
```gerlang
// Ganzzahlen
GANZ a = 10;
GANZ b = 3;
GANZ summe = a + b;        // 13
GANZ rest = a % b;         // 1

// Kommazahlen
KOMMA x = 3.14;
KOMMA y = 2.0;
KOMMA produkt = x * y;     // 6.28

// String-Verkettung mit +
WORT vorname = "Max";
WORT nachname = "Mustermann";
WORT vollname = vorname + " " + nachname;  // "Max Mustermann"
```

### Division durch Null Schutz ✅
```gerlang
GANZ sichere_division(dividend: GANZ, divisor: GANZ) {
    VERSUCHE() {
        ZURÜCK dividend / divisor;
    } FANGE fehler {
        DRUCKE("Division durch Null verhindert!");
        ZURÜCK 0;
    }
}
```

---

## 🔍 Vergleichsoperatoren

| Operator | Bedeutung           | Beispiel      | Ergebnis |
|----------|-------------------|---------------|----------|
| `==`     | Gleichheit        | `5 == 5`      | `JA`     |
| `!=`     | Ungleichheit      | `5 != 3`      | `JA`     |
| `<`      | Kleiner als       | `3 < 5`       | `JA`     |
| `>`      | Größer als        | `7 > 4`       | `JA`     |
| `<=`     | Kleiner oder gleich| `5 <= 5`     | `JA`     |
| `>=`     | Größer oder gleich | `8 >= 6`     | `JA`     |

### Beispiele
```gerlang
GANZ alter = 25;
JAIN erwachsen = alter >= 18;        // JA
JAIN teenager = alter >= 13 UND alter <= 19;  // NEIN

// String-Vergleiche
WORT passwort = "geheim123";
JAIN korrekt = passwort == "geheim123";  // JA
```

---

## 🧠 Logische Operatoren

### Deutsche Syntax
| Operator | Bedeutung    | Englisch | Beispiel                    |
|----------|--------------|----------|----------------------------|
| `UND`    | Logisches Und| `&&`     | `JA UND NEIN` → `NEIN`     |
| `ODER`   | Logisches Oder| `\|\|`   | `JA ODER NEIN` → `JA`      |
| `NICHT`  | Logisches Nicht| `!`     | `NICHT JA` → `NEIN`        |

### Wahrheitstabellen
```gerlang
// UND (beide müssen wahr sein)
JA UND JA     // JA
JA UND NEIN   // NEIN
NEIN UND JA   // NEIN
NEIN UND NEIN // NEIN

// ODER (mindestens eine muss wahr sein)
JA ODER JA     // JA
JA ODER NEIN   // JA
NEIN ODER JA   // JA
NEIN ODER NEIN // NEIN

// NICHT (invertiert den Wert)
NICHT JA   // NEIN
NICHT NEIN // JA
```

### Komplexe Bedingungen
```gerlang
GANZ alter = 20;
JAIN hat_fuehrerschein = JA;
JAIN hat_auto = NEIN;

JAIN kann_fahren = (alter >= 18) UND hat_fuehrerschein UND hat_auto;

WENN (kann_fahren) {
    DRUCKE("Du kannst Auto fahren!");
} SONST {
    DRUCKE("Du kannst noch nicht fahren.");
}
```

---

## 🎯 Zugriffs-Operatoren

### Array-Zugriff
```gerlang
KISTE zahlen = [1, 2, 3, 4, 5];
GANZ erstes = zahlen[0];           // 1
GANZ letztes = zahlen[4];          // 5

// Mehrdimensionale Arrays
KISTE matrix = [[1, 2], [3, 4]];
GANZ wert = matrix[1][0];          // 3
matrix[0][1] = 99;                 // Zuweisung
```

### Methoden-Zugriff
```gerlang
KISTE liste = [1, 2, 3];
GANZ anzahl = liste.LÄNGE;         // Property-Zugriff
liste.ERWEITERN(4);                // Methoden-Aufruf

WORT text = "Hallo";
GANZ länge = text.LÄNGE;           // 5
```

---

## ⚖️ Operator-Priorität

### Prioritätsliste (höchste zu niedrigste)
1. **Klammern**: `()`
2. **Array-Zugriff**: `[]`
3. **Methoden**: `.METHODE()`
4. **Unäre Operatoren**: `NICHT`, `-` (Minus)
5. **Multiplikation/Division**: `*`, `/`, `%`
6. **Addition/Subtraktion**: `+`, `-`
7. **Vergleiche**: `<`, `>`, `<=`, `>=`
8. **Gleichheit**: `==`, `!=`
9. **Logisches UND**: `UND`
10. **Logisches ODER**: `ODER`
11. **Zuweisung**: `=`

### Beispiele mit Priorität
```gerlang
// Ohne Klammern (folgt Priorität)
GANZ result = 2 + 3 * 4;          // 14 (nicht 20!)
JAIN bedingung = 5 > 3 UND 2 < 4; // JA

// Mit Klammern (explizite Gruppierung)
GANZ result2 = (2 + 3) * 4;       // 20
JAIN bedingung2 = (5 > 3) UND (2 < 4); // JA (redundant, aber klarer)
```

---

## 🚀 Erweiterte Beispiele

### Mathematische Berechnungen
```gerlang
KOMMA kreisflaeche(radius: KOMMA) {
    KOMMA PI = 3.14159;
    ZURÜCK PI * radius * radius;
}

GANZ fakultaet(n: GANZ) {
    WENN (n <= 1) {
        ZURÜCK 1;
    }
    ZURÜCK n * fakultaet(n - 1);
}
```

### Komplexe Bedingungen
```gerlang
JAIN ist_schaltjahr(jahr: GANZ) {
    ZURÜCK (jahr % 4 == 0) UND 
           ((jahr % 100 != 0) ODER (jahr % 400 == 0));
}

GANZ haupt() {
    GANZ jahr = 2024;
    WENN (ist_schaltjahr(jahr)) {
        DRUCKE(jahr + " ist ein Schaltjahr!");
    }
    ZURÜCK 0;
}
```

### Array-Manipulationen
```gerlang
GANZ summe_array(zahlen: KISTE) {
    GANZ summe = 0;
    FÜR (GANZ i = 0; i < zahlen.LÄNGE; i = i + 1) {
        summe = summe + zahlen[i];
    }
    ZURÜCK summe;
}

GANZ haupt() {
    KISTE meine_zahlen = [1, 2, 3, 4, 5];
    GANZ gesamt = summe_array(meine_zahlen);  // 15
    DRUCKE("Summe: " + gesamt);
    ZURÜCK 0;
}
```

---

**Tipp:** Nutze Klammern für bessere Lesbarkeit, auch wenn sie nicht zwingend nötig sind! 🎯
WENN ((a > 0 UND b > 0) ODER (a == b)) {
  DRUCKE("Bedingung erfüllt");
}
```

---

Weitere Operatoren und Beispiele findest du in den Kapiteln zu Kontrollstrukturen und Arrays.
