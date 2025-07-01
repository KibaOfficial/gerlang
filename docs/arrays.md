# 📊 GerLang – Arrays (KISTE)

> Arrays in GerLang sind flexible, mehrdimensionale Datenstrukturen mit eingebauten Methoden für effiziente Datenverarbeitung.

---

## 🏗️ Definition & Grundlagen

### Einfache Arrays
```gerlang
// Array-Deklaration mit Initialisierung
KISTE zahlen = [1, 2, 3, 4, 5];
KISTE namen = ["Alice", "Bob", "Charlie"];
KISTE gemischt = [1, "zwei", 3.14, JA];  // Verschiedene Typen möglich
KISTE leer = [];                          // Leeres Array
```

### Mehrdimensionale Arrays
```gerlang
// 2D-Array (Matrix)
KISTE matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];

// 3D-Array (Würfel)
KISTE würfel = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
];

// Unregelmäßige Arrays (Jagged Arrays)
KISTE jagged = [
    [1, 2],
    [3, 4, 5, 6],
    [7]
];
```

---

## 🎯 Zugriff auf Elemente

### Indexbasierter Zugriff
```gerlang
KISTE zahlen = [10, 20, 30, 40, 50];

// Lesen (Index beginnt bei 0)
GANZ erstes = zahlen[0];        // 10
GANZ drittes = zahlen[2];       // 30
GANZ letztes = zahlen[4];       // 50

// Schreiben/Zuweisen
zahlen[1] = 99;                 // [10, 99, 30, 40, 50]
```

### Mehrdimensionaler Zugriff
```gerlang
KISTE matrix = [[1,2,3], [4,5,6], [7,8,9]];

// Lesen
GANZ wert = matrix[1][2];       // 6 (Zeile 1, Spalte 2)
KISTE zeile = matrix[0];        // [1, 2, 3] (ganze erste Zeile)

// Schreiben
matrix[0][1] = 99;              // [[1,99,3], [4,5,6], [7,8,9]]
matrix[2] = [100, 200, 300];    // Ganze Zeile ersetzen
```

---

## ⚙️ Array-Methoden

### Größe & Information
```gerlang
KISTE liste = [1, 2, 3, 4, 5];

GANZ anzahl = liste.LÄNGE;      // 5
DRUCKE("Array hat " + anzahl + " Elemente");
```

### Elemente hinzufügen
```gerlang
KISTE liste = [2, 3, 4];

// Am Anfang hinzufügen
liste.HINZUFÜGEN(1);            // [1, 2, 3, 4]

// Am Ende anhängen  
liste.ERWEITERN(5);             // [1, 2, 3, 4, 5]
liste.ERWEITERN(6);             // [1, 2, 3, 4, 5, 6]

DRUCKE("Neue Länge: " + liste.LÄNGE);  // 6
```

### 🔮 Zukünftige Methoden (geplant)
```gerlang
// Diese Methoden sind für zukünftige Versionen geplant:
liste.SORTIEREN();              // Sortiert das Array
liste.UMKEHREN();               // Kehrt die Reihenfolge um
GANZ index = liste.FINDEN(3);   // Findet Index von Element
KISTE neu = liste.FILTERN(x -> x > 2);  // Filtert Elemente
```

---

## 🔄 Iteration & Schleifen

### For-Schleife mit Index
```gerlang
KISTE früchte = ["Apfel", "Banane", "Orange", "Traube"];

FÜR (GANZ i = 0; i < früchte.LÄNGE; i = i + 1) {
    DRUCKE("Frucht " + i + ": " + früchte[i]);
}
```

### Mehrdimensionale Iteration
```gerlang
KISTE matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];

// Alle Elemente durchlaufen
FÜR (GANZ zeile = 0; zeile < matrix.LÄNGE; zeile = zeile + 1) {
    FÜR (GANZ spalte = 0; spalte < matrix[zeile].LÄNGE; spalte = spalte + 1) {
        DRUCKE("matrix[" + zeile + "][" + spalte + "] = " + matrix[zeile][spalte]);
    }
}
```

---

## 💡 Praktische Beispiele

### Array-Summe berechnen
```gerlang
GANZ summe_berechnen(zahlen: KISTE) {
    GANZ summe = 0;
    FÜR (GANZ i = 0; i < zahlen.LÄNGE; i = i + 1) {
        summe = summe + zahlen[i];
    }
    ZURÜCK summe;
}

GANZ haupt() {
    KISTE werte = [10, 20, 30, 40, 50];
    GANZ total = summe_berechnen(werte);
    DRUCKE("Summe: " + total);  // 150
    ZURÜCK 0;
}
```

### Matrix-Multiplikation (vereinfacht)
```gerlang
NIX matrix_ausgeben(m: KISTE) {
    FÜR (GANZ i = 0; i < m.LÄNGE; i = i + 1) {
        WORT zeile = "";
        FÜR (GANZ j = 0; j < m[i].LÄNGE; j = j + 1) {
            zeile = zeile + m[i][j] + " ";
        }
        DRUCKE(zeile);
    }
}

GANZ haupt() {
    KISTE matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ];
    
    DRUCKE("Matrix:");
    matrix_ausgeben(matrix);
    ZURÜCK 0;
}
```

### Tic-Tac-Toe Spielfeld
```gerlang
KISTE spielfeld = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
];

NIX spielfeld_anzeigen() {
    DRUCKE("  0   1   2");
    FÜR (GANZ i = 0; i < 3; i = i + 1) {
        WORT zeile = i + " ";
        FÜR (GANZ j = 0; j < 3; j = j + 1) {
            zeile = zeile + spielfeld[i][j];
            WENN (j < 2) {
                zeile = zeile + " | ";
            }
        }
        DRUCKE(zeile);
        WENN (i < 2) {
            DRUCKE("  ---------");
        }
    }
}

GANZ haupt() {
    // Einige Züge simulieren
    spielfeld[0][0] = "X";
    spielfeld[1][1] = "O";
    spielfeld[2][2] = "X";
    
    spielfeld_anzeigen();
    ZURÜCK 0;
}
```

---

## ⚠️ Wichtige Hinweise

### Array-Grenzen
```gerlang
KISTE kleine_liste = [1, 2, 3];

// ✅ Gültige Indizes: 0, 1, 2
GANZ ok = kleine_liste[0];      // OK

// ❌ Ungültige Indizes führen zu Runtime-Fehlern
// GANZ fehler = kleine_liste[5];  // RuntimeError!
```

### Fehlerbehandlung bei Arrays
```gerlang
GANZ sicherer_zugriff(arr: KISTE, index: GANZ) {
    VERSUCHE() {
        ZURÜCK arr[index];
    } FANGE fehler {
        DRUCKE("Ungültiger Array-Index: " + index);
        ZURÜCK 0;  // Standardwert
    }
}
```

### Performance-Tipps
- Arrays wachsen dynamisch, aber häufiges `.ERWEITERN()` kann langsam sein
- Mehrdimensionale Arrays sind eigentlich Arrays von Arrays
- Verwende `.LÄNGE` anstatt magische Zahlen für Schleifen

---

## 🚀 Weiterführende Themen

- 📖 [Funktionen mit Array-Parametern](funktionen.md)
- 🔧 [Array-Methoden im Detail](datentypen.md) 
- 💡 [Praktische Beispiele](BEISPIELE.md)
- 🆘 [Häufige Array-Fehler](faq.md)

---

**Arrays sind das Herzstück vieler GerLang-Programme – nutze sie weise! 📊**
