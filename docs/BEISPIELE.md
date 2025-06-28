# GerLang – Beispielprogramme

Hier findest du kommentierte Beispielprogramme für verschiedene Sprachfeatures.

---

## 1. Methoden für Datentypen (KISTE/WORT)
```gerlang
KISTE liste = [1,2];
liste.HINZUFÜGEN(0); // liste = [0,1,2]
liste.ERWEITERN(3);  // liste = [0,1,2,3]
DRUCKE(liste.LÄNGE); // Ausgabe: 4

WORT text = "Hallo Welt";
DRUCKE(text.LÄNGE); // Ausgabe: 10
```

---

## 2. Mehrdimensionale Arrays und Zuweisung an Array-Elemente
```gerlang
KISTE matrix = [[1,2],[3,4]];
matrix[0][1] = 99;
DRUCKE(matrix[0][1]); // Ausgabe: 99
```

---

## 3. Zuweisung an beliebige Ausdrücke
```gerlang
KISTE zahlen = [1,2,3];
zahlen[1] = 42;
DRUCKE(zahlen); // Ausgabe: [1, 42, 3]
```

---

## 4. Fibonacci (Rekursion)
```gerlang
GANZ fib(n: GANZ) {
  WENN (n < 2) {
    ZURÜCK n;
  }
  ZURÜCK fib(n-1) + fib(n-2);
}
GANZ haupt() {
  DRUCKE("Fibonacci(10):");
  DRUCKE(fib(10));
  ZURÜCK 0;
}
```

---

## 5. Funktionen und Ausgabe
```gerlang
GANZ add(a: GANZ, b: GANZ) {
  ZURÜCK a+b;
}
GANZ haupt() {
  DRUCKE("Hallo, Welt!");
  DRUCKE(add(1,2));
  ZURÜCK 0;
}
```

---

## 6. Kontrollstrukturen und Variablen
```gerlang
GANZ haupt() {
    DRUCKE("Hallo, Welt!");
    GANZ zahl = 42;
    JAIN wahrheit = JA;
    KOMMA pi = 3.14;
    WENN (wahrheit) {
        DRUCKE("Es ist wahr!");
    } SONST {
        DRUCKE("Es ist nicht wahr!");
    }
    FÜR (GANZ i = 0; i < 3; i = i + 1) {
        DRUCKE("Zähler: " + i);
    }
    SOLANGE (zahl > 0) {
        DRUCKE("Runterzählen: " + zahl);
        zahl = zahl - 1;
    }
    ZURÜCK 0;
}
```

---

## 7. Test für Arrays und Logik
```gerlang
KISTE zahlen = [1, 2, 3, 4, 5];
GANZ summe(arr: KISTE) {
  GANZ s = 0;
  FÜR (GANZ i = 0; i < 5; i = i + 1) {
    s = s + arr[i];
  }
  ZURÜCK s;
}
GANZ test_logik(a: GANZ, b: GANZ) {
  WENN ((a > 0 UND b > 0) ODER (a == b)) {
    ZURÜCK 1;
  } SONST {
    ZURÜCK 0;
  }
}
GANZ haupt() {
  DRUCKE("Summe der Zahlen:");
  DRUCKE(summe(zahlen));
  DRUCKE("Logik-Test (2,2):");
  DRUCKE(test_logik(2,2));
  DRUCKE("Logik-Test (2,-1):");
  DRUCKE(test_logik(2,-1));
  ZURÜCK 0;
}
```

---

Weitere Beispiele findest du in den Dateien `examples/` und im FAQ.
