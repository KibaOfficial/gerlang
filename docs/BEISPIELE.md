# GerLang – Beispielprogramme

Hier findest du kommentierte Beispielprogramme für verschiedene Sprachfeatures.

## 📚 Inhaltsverzeichnis

1. [Grundlagen und Variablen](#grundlagen)
2. [Funktionen und Rekursion](#funktionen)
3. [Arrays und Methoden](#arrays)
4. [Kontrollstrukturen](#kontrollstrukturen)
5. [Fehlerbehandlung](#fehlerbehandlung)
6. [Modulare Programmierung](#module)
7. [Interaktive Programme](#interaktiv)

---

## <a id="grundlagen"></a>1. Grundlagen und Variablen

### Einfaches Hallo-Welt-Programm
```gerlang
GANZ haupt() {
    DRUCKE("Hallo, Welt!");
    ZURÜCK 0;
}
```

### Verschiedene Datentypen
```gerlang
GANZ haupt() {
    GANZ zahl = 42;
    KOMMA pi = 3.14159;
    WORT text = "GerLang ist toll!";
    JAIN wahrheit = JA;
    
    // Klassische String-Concatenation
    DRUCKE("Ganze Zahl: " + zahl);
    DRUCKE("Kommazahl: " + pi);
    
    // Moderne String-Interpolation (V4.0+)
    DRUCKE("Text: ${text}");
    DRUCKE("Wahrheitswert: ${wahrheit}");
    DRUCKE("Berechnung: ${zahl + 8} = ${zahl} + 8");
    
    ZURÜCK 0;
}
```

### String-Interpolation Beispiele
```gerlang
GANZ haupt() {
    WORT name = "Max";
    GANZ alter = 25;
    KISTE hobbys = ["Programmieren", "Lesen", "Sport"];
    
    // Einfache Variablen
    DRUCKE("Hallo ${name}!");
    
    // Komplexe Ausdrücke
    DRUCKE("${name} ist ${alter} Jahre alt und wird ${alter + 1} Jahre alt");
    
    // Methoden-Aufrufe
    DRUCKE("${name} hat ${hobbys.LÄNGE} Hobbys: ${hobbys}");
    
    // Verschachtelte Templates
    GANZ jahr = 2025;
    DRUCKE("In ${jahr + 10} bin ich ${alter + 10} Jahre alt");
    
    ZURÜCK 0;
}
```

---

## <a id="funktionen"></a>2. Funktionen und Rekursion

### Einfache Funktion
```gerlang
GANZ addiere(a: GANZ, b: GANZ) {
    ZURÜCK a + b;
}

GANZ haupt() {
    GANZ ergebnis = addiere(15, 27);
    DRUCKE("15 + 27 = " + ergebnis);
    ZURÜCK 0;
}
```

### Fibonacci-Zahlen (Rekursion)
```gerlang
GANZ fibonacci(n: GANZ) {
    WENN (n <= 1) {
        ZURÜCK n;
    }
    ZURÜCK fibonacci(n-1) + fibonacci(n-2);
}

GANZ haupt() {
    DRUCKE("Fibonacci-Zahlen:");
    FÜR (GANZ i = 0; i < 10; i = i + 1) {
        DRUCKE("fib(" + i + ") = " + fibonacci(i));
    }
    ZURÜCK 0;
}
```

### Fakultät berechnen
```gerlang
GANZ fakultaet(n: GANZ) {
    WENN (n <= 1) {
        ZURÜCK 1;
    }
    ZURÜCK n * fakultaet(n - 1);
}

GANZ haupt() {
    GANZ zahl = 5;
    DRUCKE(zahl + "! = " + fakultaet(zahl));
    ZURÜCK 0;
}
```
---

## <a id="arrays"></a>3. Arrays und Methoden

### Methoden für Arrays (KISTE)
```gerlang
GANZ haupt() {
    KISTE liste = [1, 2, 3];
    
    // Array-Methoden verwenden
    DRUCKE("Ursprüngliche Liste: " + liste);
    DRUCKE("Länge: " + liste.LÄNGE);
    
    liste.HINZUFÜGEN(4);
    DRUCKE("Nach HINZUFÜGEN(4): " + liste);
    
    liste.ERWEITERN(5);
    DRUCKE("Nach ERWEITERN(5): " + liste);
    
    ZURÜCK 0;
}
```

### Mehrdimensionale Arrays
```gerlang
GANZ haupt() {
    // 2D-Array erstellen
    KISTE matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
    
    // Zugriff auf Elemente
    DRUCKE("Element [1][2]: " + matrix[1][2]); // Ausgabe: 6
    
    // Element ändern
    matrix[0][1] = 99;
    DRUCKE("Nach Änderung: " + matrix[0]); // Ausgabe: [1, 99, 3]
    
    ZURÜCK 0;
}
```

### String-Methoden (WORT)
```gerlang
GANZ haupt() {
    WORT text = "Hallo Welt";
    
    DRUCKE("Text: " + text);
    DRUCKE("Länge: " + text.LÄNGE);
    
    ZURÜCK 0;
}
```

---

## <a id="kontrollstrukturen"></a>4. Kontrollstrukturen

### If-Else Bedingungen
```gerlang
GANZ bewerte_note(note: GANZ) {
    WENN (note >= 90) {
        DRUCKE("Sehr gut!");
    } SONST WENN (note >= 80) {
        DRUCKE("Gut!");
    } SONST WENN (note >= 70) {
        DRUCKE("Befriedigend!");
    } SONST WENN (note >= 60) {
        DRUCKE("Ausreichend!");
    } SONST {
        DRUCKE("Ungenügend!");
    }
    ZURÜCK 0;
}

GANZ haupt() {
    bewerte_note(85);
    bewerte_note(55);
    ZURÜCK 0;
}
```

### For-Schleifen
```gerlang
GANZ haupt() {
    DRUCKE("Zähle von 1 bis 10:");
    FÜR (GANZ i = 1; i <= 10; i = i + 1) {
        DRUCKE("Zahl: " + i);
    }
    
    // Array durchlaufen
    KISTE farben = ["rot", "grün", "blau"];
    DRUCKE("\nFarben:");
    FÜR (GANZ i = 0; i < farben.LÄNGE; i = i + 1) {
        DRUCKE((i + 1) + ". " + farben[i]);
    }
    
    ZURÜCK 0;
}
```

### While-Schleifen
```gerlang
GANZ haupt() {
    GANZ zahl = 10;
    
    DRUCKE("Countdown:");
    SOLANGE (zahl > 0) {
        DRUCKE(zahl);
        zahl = zahl - 1;
    }
    DRUCKE("Start!");
    
    ZURÜCK 0;
}
```

### Logische Operatoren
```gerlang
JAIN ist_erwachsen(alter: GANZ) {
    ZURÜCK alter >= 18;
}

JAIN kann_wählen(alter: GANZ, staatsbuerger: JAIN) {
    ZURÜCK ist_erwachsen(alter) UND staatsbuerger;
}

GANZ haupt() {
    GANZ alter = 20;
    JAIN staatsbuerger = JA;
    
    WENN (kann_wählen(alter, staatsbuerger)) {
        DRUCKE("Du darfst wählen!");
    } SONST {
        DRUCKE("Du darfst noch nicht wählen.");
    }
    
    ZURÜCK 0;
}
```

---

## <a id="fehlerbehandlung"></a>5. Fehlerbehandlung

### Try-Catch Mechanismus
```gerlang
GANZ teile_sicher(a: GANZ, b: GANZ) {
    VERSUCHE() {
        GANZ ergebnis = a / b;
        DRUCKE(a + " / " + b + " = " + ergebnis);
        ZURÜCK ergebnis;
    } FANGE fehler {
        DRUCKE("Fehler beim Teilen: " + fehler);
        ZURÜCK 0;
    }
}

GANZ haupt() {
    DRUCKE("Sichere Division:");
    teile_sicher(10, 2);    // Funktioniert
    teile_sicher(10, 0);    // Wirft Fehler
    
    ZURÜCK 0;
}
```

### Erweiterte Fehlerbehandlung
```gerlang
GANZ verarbeite_array(arr: KISTE, index: GANZ) {
    VERSUCHE() {
        DRUCKE("Element an Index " + index + ": " + arr[index]);
        ZURÜCK arr[index];
    } FANGE fehler {
        DRUCKE("Fehler beim Array-Zugriff: " + fehler);
        DRUCKE("Index " + index + " ist nicht gültig!");
        ZURÜCK -1;
    }
}

GANZ haupt() {
    KISTE zahlen = [10, 20, 30];
    
    verarbeite_array(zahlen, 1);  // Funktioniert
    verarbeite_array(zahlen, 5);  // Index außerhalb des Bereichs
    
    ZURÜCK 0;
}
```

---

## <a id="module"></a>6. Modulare Programmierung

### Modul erstellen (math_utils.gerl)
```gerlang
// math_utils.gerl - Mathematische Hilfsfunktionen
GIBFREI GANZ quadrat(x: GANZ) {
    ZURÜCK x * x;
}

GIBFREI GANZ potenz(basis: GANZ, exponent: GANZ) {
    GANZ ergebnis = 1;
    FÜR (GANZ i = 0; i < exponent; i = i + 1) {
        ergebnis = ergebnis * basis;
    }
    ZURÜCK ergebnis;
}

GIBFREI GANZ max(a: GANZ, b: GANZ) {
    WENN (a > b) {
        ZURÜCK a;
    } SONST {
        ZURÜCK b;
    }
}

// Mehrere Funktionen gleichzeitig exportieren
GIBFREI quadrat, potenz, max;
```

### Modul verwenden (hauptprogramm.gerl)
```gerlang
// hauptprogramm.gerl
HOLE quadrat, potenz, max VON "math_utils.gerl";

GANZ haupt() {
    GANZ a = 5;
    GANZ b = 3;
    
    DRUCKE("Quadrat von " + a + " = " + quadrat(a));
    DRUCKE(a + " hoch " + b + " = " + potenz(a, b));
    DRUCKE("Maximum von " + a + " und " + b + " = " + max(a, b));
    
    ZURÜCK 0;
}
```

---

## <a id="interaktiv"></a>7. Interaktive Programme

### Einfache Benutzereingabe
```gerlang
GANZ haupt() {
    DRUCKE("Wie heißt du?");
    WORT name = LESE();
    DRUCKE("Hallo, " + name + "!");
    
    DRUCKE("Wie alt bist du?");
    WORT eingabe = LESE();
    GANZ alter = GANZ(eingabe);  // String zu Zahl konvertieren
    
    WENN (alter >= 18) {
        DRUCKE("Du bist volljährig!");
    } SONST {
        DRUCKE("Du bist noch minderjährig.");
    }
    
    ZURÜCK 0;
}
```

### Interaktiver Taschenrechner
```gerlang
KOMMA rechne(a: KOMMA, operator: WORT, b: KOMMA) {
    WENN (operator == "+") {
        ZURÜCK a + b;
    } SONST WENN (operator == "-") {
        ZURÜCK a - b;
    } SONST WENN (operator == "*") {
        ZURÜCK a * b;
    } SONST WENN (operator == "/") {
        WENN (b != 0) {
            ZURÜCK a / b;
        } SONST {
            DRUCKE("Fehler: Division durch Null!");
            ZURÜCK 0;
        }
    } SONST {
        DRUCKE("Unbekannter Operator: " + operator);
        ZURÜCK 0;
    }
}

GANZ haupt() {
    DRUCKE("=== Einfacher Taschenrechner ===");
    
    DRUCKE("Erste Zahl:");
    KOMMA zahl1 = KOMMA(LESE());
    
    DRUCKE("Operator (+, -, *, /):");
    WORT op = LESE();
    
    DRUCKE("Zweite Zahl:");
    KOMMA zahl2 = KOMMA(LESE());
    
    KOMMA ergebnis = rechne(zahl1, op, zahl2);
    DRUCKE("Ergebnis: " + zahl1 + " " + op + " " + zahl2 + " = " + ergebnis);
    
    ZURÜCK 0;
}
```

### Zahlenratespiel
```gerlang
GANZ haupt() {
    GANZ geheimzahl = 42;  // In echtem Spiel wäre das zufällig
    GANZ versuche = 0;
    GANZ maxVersuche = 5;
    JAIN erraten = NEIN;
    
    DRUCKE("=== Zahlenratespiel ===");
    DRUCKE("Ich denke an eine Zahl zwischen 1 und 100.");
    DRUCKE("Du hast " + maxVersuche + " Versuche!");
    
    SOLANGE (versuche < maxVersuche UND erraten == NEIN) {
        versuche = versuche + 1;
        DRUCKE("\nVersuch " + versuche + ":");
        DRUCKE("Deine Zahl:");
        
        GANZ tipp = GANZ(LESE());
        
        WENN (tipp == geheimzahl) {
            DRUCKE("🎉 Richtig! Du hast gewonnen!");
            erraten = JA;
        } SONST WENN (tipp < geheimzahl) {
            DRUCKE("📈 Zu niedrig!");
        } SONST {
            DRUCKE("📉 Zu hoch!");
        }
    }
    
    WENN (erraten == NEIN) {
        DRUCKE("\n😞 Verloren! Die Zahl war " + geheimzahl);
    }
    
    ZURÜCK 0;
}
```

---

## 🔗 Weitere Ressourcen

- Mehr Beispiele findest du im `examples/` Verzeichnis
- Siehe auch: [Sprachreferenz](SPRACHE.md)
- Funktionen im Detail: [funktionen.md](funktionen.md)
- Arrays und Methoden: [arrays.md](arrays.md)
- Fehlerbehandlung: [fehlerbehandlung.md](fehlerbehandlung.md)
- Modulare Programmierung: [modulsystem.md](modulsystem.md)
