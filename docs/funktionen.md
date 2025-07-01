# 🔧 GerLang – Funktionen

> Funktionen sind die Bausteine moderner GerLang-Programme. Sie ermöglichen Wiederverwendbarkeit, Modularität und strukturierte Programmierung.

---

## 📋 Grundlagen

### Funktionsdefinition
```gerlang
RÜCKGABETYP funktionsname(parameter1: TYP, parameter2: TYP) {
    // Funktionskörper
    ZURÜCK wert;  // Optional bei NIX-Funktionen
}
```

### Hauptfunktion (Pflicht)
Jedes GerLang-Programm benötigt eine `haupt()`-Funktion:
```gerlang
GANZ haupt() {
    DRUCKE("Hallo, Welt!");
    ZURÜCK 0;  // Exit-Code (0 = Erfolg)
}
```

---

## 🎯 Rückgabetypen

| Typ     | Bedeutung              | Beispiel                    |
|---------|------------------------|-----------------------------|
| `GANZ`  | Gibt Ganzzahl zurück   | `GANZ addiere(a, b)`       |
| `KOMMA` | Gibt Kommazahl zurück  | `KOMMA berechne_pi()`      |
| `WORT`  | Gibt String zurück     | `WORT begrüßung(name)`     |
| `JAIN`  | Gibt Boolean zurück    | `JAIN ist_gerade(zahl)`    |
| `KISTE` | Gibt Array zurück      | `KISTE erstelle_liste()`   |
| `NIX`   | Kein Rückgabewert      | `NIX drucke_info()`        |

---

## ⚙️ Parameter & Argumente

### Einfache Parameter
```gerlang
// Funktion mit zwei Parametern
GANZ addiere(a: GANZ, b: GANZ) {
    ZURÜCK a + b;
}

// Funktion ohne Parameter
WORT aktuelle_zeit() {
    ZURÜCK "12:00 Uhr";  // Vereinfacht
}

// Aufruf
GANZ haupt() {
    GANZ summe = addiere(5, 3);        // 8
    WORT zeit = aktuelle_zeit();       // "12:00 Uhr"
    DRUCKE("Summe: " + summe);
    DRUCKE("Zeit: " + zeit);
    ZURÜCK 0;
}
```

### Arrays als Parameter
```gerlang
// Array-Parameter (Pass-by-Reference)
GANZ summe_berechnen(zahlen: KISTE) {
    GANZ total = 0;
    FÜR (GANZ i = 0; i < zahlen.LÄNGE; i = i + 1) {
        total = total + zahlen[i];
    }
    ZURÜCK total;
}

// Array zurückgeben
KISTE verdopple_werte(original: KISTE) {
    KISTE neu = [];
    FÜR (GANZ i = 0; i < original.LÄNGE; i = i + 1) {
        neu.ERWEITERN(original[i] * 2);
    }
    ZURÜCK neu;
}

GANZ haupt() {
    KISTE werte = [1, 2, 3, 4, 5];
    GANZ summe = summe_berechnen(werte);           // 15
    KISTE doppelt = verdopple_werte(werte);        // [2, 4, 6, 8, 10]
    
    DRUCKE("Original: " + werte);
    DRUCKE("Summe: " + summe);
    DRUCKE("Verdoppelt: " + doppelt);
    ZURÜCK 0;
}
```

### Gemischte Parameter
```gerlang
// Verschiedene Parametertypen
WORT formatiere_nachricht(name: WORT, alter: GANZ, aktiv: JAIN) {
    WORT status = aktiv ? "aktiv" : "inaktiv";
    ZURÜCK name + " (" + alter + " Jahre, " + status + ")";
}

GANZ haupt() {
    WORT nachricht = formatiere_nachricht("Alice", 25, JA);
    DRUCKE(nachricht);  // "Alice (25 Jahre, aktiv)"
    ZURÜCK 0;
}
```

---

## 🔄 Rekursion

### Fakultät berechnen
```gerlang
GANZ fakultät(n: GANZ) {
    // Basis-Fall
    WENN (n <= 1) {
        ZURÜCK 1;
    }
    // Rekursiver Fall
    ZURÜCK n * fakultät(n - 1);
}

GANZ haupt() {
    DRUCKE("5! = " + fakultät(5));     // 120
    DRUCKE("10! = " + fakultät(10));   // 3628800
    ZURÜCK 0;
}
```

### Fibonacci-Zahlen
```gerlang
GANZ fibonacci(n: GANZ) {
    WENN (n <= 1) {
        ZURÜCK n;
    }
    ZURÜCK fibonacci(n - 1) + fibonacci(n - 2);
}

// Optimierte Version mit Array
GANZ fibonacci_optimiert(n: GANZ) {
    WENN (n <= 1) {
        ZURÜCK n;
    }
    
    KISTE fib = [0, 1];
    FÜR (GANZ i = 2; i <= n; i = i + 1) {
        GANZ nächste = fib[i-1] + fib[i-2];
        fib.ERWEITERN(nächste);
    }
    ZURÜCK fib[n];
}

GANZ haupt() {
    DRUCKE("Fibonacci(10) = " + fibonacci(10));              // 55
    DRUCKE("Fibonacci optimiert(10) = " + fibonacci_optimiert(10));  // 55
    ZURÜCK 0;
}
```

### Binary Search (Rekursiv)
```gerlang
GANZ binary_search(arr: KISTE, ziel: GANZ, links: GANZ, rechts: GANZ) {
    WENN (links > rechts) {
        ZURÜCK -1;  // Nicht gefunden
    }
    
    GANZ mitte = (links + rechts) / 2;
    
    WENN (arr[mitte] == ziel) {
        ZURÜCK mitte;
    } SONST WENN (arr[mitte] > ziel) {
        ZURÜCK binary_search(arr, ziel, links, mitte - 1);
    } SONST {
        ZURÜCK binary_search(arr, ziel, mitte + 1, rechts);
    }
}

GANZ haupt() {
    KISTE sortiert = [1, 3, 5, 7, 9, 11, 13, 15];
    GANZ index = binary_search(sortiert, 7, 0, sortiert.LÄNGE - 1);
    DRUCKE("Index von 7: " + index);  // 3
    ZURÜCK 0;
}
```

---

## 🛡️ Fehlerbehandlung in Funktionen

### Defensive Programmierung
```gerlang
GANZ sichere_division(dividend: GANZ, divisor: GANZ) {
    // Input-Validierung
    WENN (divisor == 0) {
        DRUCKE("⚠️ Warnung: Division durch Null!");
        ZURÜCK 0;  // Sicherer Standardwert
    }
    
    ZURÜCK dividend / divisor;
}

// Mit Exception-Handling
GANZ strenge_division(dividend: GANZ, divisor: GANZ) {
    VERSUCHE() {
        WENN (divisor == 0) {
            MECKER("Division durch Null ist nicht erlaubt!");
        }
        ZURÜCK dividend / divisor;
    } FANGE fehler {
        DRUCKE("Division fehlgeschlagen: " + fehler);
        ZURÜCK 0;
    }
}
```

### Array-Funktionen mit Validierung
```gerlang
GANZ get_element(arr: KISTE, index: GANZ) {
    // Index-Validierung
    WENN (index < 0 ODER index >= arr.LÄNGE) {
        DRUCKE("⚠️ Index " + index + " außerhalb der Array-Grenzen (0-" + (arr.LÄNGE-1) + ")");
        ZURÜCK -1;  // Fehlerindikator
    }
    ZURÜCK arr[index];
}

NIX set_element(arr: KISTE, index: GANZ, wert: GANZ) {
    WENN (index < 0 ODER index >= arr.LÄNGE) {
        DRUCKE("❌ Kann Element nicht setzen: Index außerhalb der Grenzen");
        ZURÜCK;
    }
    arr[index] = wert;
    DRUCKE("✅ Element gesetzt: arr[" + index + "] = " + wert);
}
```

---

## 📊 Praktische Beispiele

### Mathematische Funktionen
```gerlang
// Potenz-Funktion
GANZ potenz(basis: GANZ, exponent: GANZ) {
    GANZ result = 1;
    FÜR (GANZ i = 0; i < exponent; i = i + 1) {
        result = result * basis;
    }
    ZURÜCK result;
}

// Größter gemeinsamer Teiler (GCD)
GANZ gcd(a: GANZ, b: GANZ) {
    SOLANGE (b != 0) {
        GANZ temp = b;
        b = a % b;
        a = temp;
    }
    ZURÜCK a;
}

// Primzahl-Test
JAIN ist_primzahl(n: GANZ) {
    WENN (n <= 1) {
        ZURÜCK NEIN;
    }
    FÜR (GANZ i = 2; i * i <= n; i = i + 1) {
        WENN (n % i == 0) {
            ZURÜCK NEIN;
        }
    }
    ZURÜCK JA;
}
```

### String-Verarbeitung
```gerlang
GANZ zähle_zeichen(text: WORT, zeichen: WORT) {
    GANZ anzahl = 0;
    FÜR (GANZ i = 0; i < text.LÄNGE; i = i + 1) {
        WENN (text[i] == zeichen) {  // Vereinfacht
            anzahl = anzahl + 1;
        }
    }
    ZURÜCK anzahl;
}

WORT wiederhole_text(text: WORT, anzahl: GANZ) {
    WORT result = "";
    FÜR (GANZ i = 0; i < anzahl; i = i + 1) {
        result = result + text;
    }
    ZURÜCK result;
}

JAIN ist_palindrom(text: WORT) {
    GANZ länge = text.LÄNGE;
    FÜR (GANZ i = 0; i < länge / 2; i = i + 1) {
        // Vereinfachte Vergleichslogik
        WENN (text[i] != text[länge - 1 - i]) {
            ZURÜCK NEIN;
        }
    }
    ZURÜCK JA;
}
```

### Array-Algorithmen
```gerlang
// Bubble Sort
NIX bubble_sort(arr: KISTE) {
    GANZ n = arr.LÄNGE;
    FÜR (GANZ i = 0; i < n - 1; i = i + 1) {
        FÜR (GANZ j = 0; j < n - i - 1; j = j + 1) {
            WENN (arr[j] > arr[j + 1]) {
                // Tauschen
                GANZ temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

// Minimum finden
GANZ finde_minimum(arr: KISTE) {
    WENN (arr.LÄNGE == 0) {
        MECKER("Array ist leer!");
    }
    
    GANZ min = arr[0];
    FÜR (GANZ i = 1; i < arr.LÄNGE; i = i + 1) {
        WENN (arr[i] < min) {
            min = arr[i];
        }
    }
    ZURÜCK min;
}

// Array filtern
KISTE filtere_gerade(arr: KISTE) {
    KISTE result = [];
    FÜR (GANZ i = 0; i < arr.LÄNGE; i = i + 1) {
        WENN (arr[i] % 2 == 0) {
            result.ERWEITERN(arr[i]);
        }
    }
    ZURÜCK result;
}
```

---

## 🎮 Komplettes Beispiel: Zahlenraten-Spiel

```gerlang
// Zufallszahl zwischen min und max (inklusive)
GANZ zufallszahl(min: GANZ, max: GANZ) {
    // Vereinfachte Implementierung
    ZURÜCK min + (ZEIT() % (max - min + 1));
}

// Eingabe validieren und zu Zahl konvertieren
GANZ lese_zahl(prompt: WORT) {
    SOLANGE (JA) {
        WORT eingabe = LESE(prompt);
        
        VERSUCHE() {
            GANZ zahl = ZU_ZAHL(eingabe);
            ZURÜCK zahl;
        } FANGE fehler {
            DRUCKE("❌ '" + eingabe + "' ist keine gültige Zahl. Versuche es erneut.");
        }
    }
}

// Spiel-Logik
NIX spiele_zahlenraten() {
    GANZ geheimzahl = zufallszahl(1, 100);
    GANZ versuche = 0;
    GANZ max_versuche = 7;
    
    DRUCKE("🎯 === Zahlenraten-Spiel ===");
    DRUCKE("Ich denke an eine Zahl zwischen 1 und 100!");
    DRUCKE("Du hast " + max_versuche + " Versuche.");
    DRUCKE("");
    
    SOLANGE (versuche < max_versuche) {
        versuche = versuche + 1;
        GANZ tipp = lese_zahl("Versuch " + versuche + "/" + max_versuche + " - Dein Tipp: ");
        
        WENN (tipp == geheimzahl) {
            DRUCKE("🎉 RICHTIG! Du hast die Zahl " + geheimzahl + " in " + versuche + " Versuchen erraten!");
            ZURÜCK;
        } SONST WENN (tipp < geheimzahl) {
            DRUCKE("📈 Zu niedrig!");
        } SONST {
            DRUCKE("📉 Zu hoch!");
        }
        
        WENN (versuche < max_versuche) {
            GANZ verbleibend = max_versuche - versuche;
            DRUCKE("Noch " + verbleibend + " Versuche übrig.\n");
        }
    }
    
    DRUCKE("💔 Schade! Die Zahl war " + geheimzahl + ". Vielleicht beim nächsten Mal!");
}

GANZ haupt() {
    spiele_zahlenraten();
    ZURÜCK 0;
}
```

---

## 💡 Best Practices

### ✅ Do's
```gerlang
// ✅ Sprechende Funktionsnamen
JAIN ist_volljährig(alter: GANZ) { ... }
KISTE filtere_positive_zahlen(zahlen: KISTE) { ... }

// ✅ Eine Aufgabe pro Funktion
GANZ berechne_summe(zahlen: KISTE) { ... }
NIX drucke_statistiken(summe: GANZ, anzahl: GANZ) { ... }

// ✅ Input-Validierung
GANZ sichere_funktion(wert: GANZ) {
    WENN (wert < 0) {
        MECKER("Wert muss positiv sein!");
    }
    // ...
}

// ✅ Dokumentation durch Kommentare
// Berechnet die n-te Fibonacci-Zahl iterativ
// Parameter: n - Die Position in der Fibonacci-Folge (>= 0)
// Rückgabe: Die n-te Fibonacci-Zahl
GANZ fibonacci(n: GANZ) { ... }
```

### ❌ Don'ts
```gerlang
// ❌ Unklare Namen
GANZ f(x: GANZ) { ... }
GANZ berechne(a: GANZ, b: GANZ, c: GANZ) { ... }

// ❌ Zu viele Parameter
GANZ kompliziert(a: GANZ, b: GANZ, c: GANZ, d: GANZ, e: GANZ, f: GANZ) { ... }

// ❌ Fehlende Validierung
GANZ division(a: GANZ, b: GANZ) {
    ZURÜCK a / b;  // Was wenn b == 0?
}

// ❌ Zu lange Funktionen (> 20 Zeilen)
GANZ mega_funktion() {
    // 100 Zeilen Code...
}
```

---

## 🔗 Weiterführende Themen

- 📦 [Modulsystem & Export/Import](modulsystem.md)
- 📊 [Arrays & Datenstrukturen](arrays.md)
- 🛡️ [Fehlerbehandlung](fehlerbehandlung.md)
- 💡 [Praktische Beispiele](BEISPIELE.md)
- ❓ [FAQ & Troubleshooting](faq.md)

---

**Funktionen sind das Rückgrat jeder guten GerLang-Anwendung – nutze sie weise! 🔧**
