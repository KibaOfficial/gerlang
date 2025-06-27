# GerLang – Beispielprogramme

Hier findest du kommentierte Beispielprogramme für verschiedene Sprachfeatures.

---

## 1. Fibonacci (Rekursion)
```gerlang
HINWEIS: Fibonacci-Test für Funktionen und Rekursion
GANZ fib(n: GANZ) {
  WENN (n < 2) {
    ZURÜCK n;
  }
  ZURÜCK fib(n-1) + fib(n-2);
}
NIX haupt() {
  DRUCKE("Fibonacci(10):");
  DRUCKE(fib(10));
  ZURÜCK 0;
}
```

---

## 2. Funktionen und Ausgabe
```gerlang
GANZ add(a: GANZ, b: GANZ) {
  ZURÜCK a+b;
}
NIX haupt() {
  DRUCKE("Hallo, Welt!");
  DRUCKE(add(1,2));
  ZURÜCK 0;
}
```

---

## 3. Kontrollstrukturen und Variablen
```gerlang
NIX haupt() {
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
    ZURÜCK;
}
```

---

## 4. Test für Arrays und Logik
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
NIX haupt() {
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

## 5. Einfache Ausgabe und Schleifen
```gerlang
NIX haupt() {
  DRUCKE("Dies ist ein Test");
  GANZ zahl = 10;
  JAIN wahrheit = JA;
  KOMMA pi = 3.14159;
  WENN (wahrheit) {
    DRUCKE("Die Bedingung ist wahr.");
  } SONST {
    DRUCKE("Die Bedingung ist falsch.");
  }
  DRUCKE("Der Wert von pi ist: " + pi);
  DRUCKE("Die Zahl ist: " + zahl);
  FÜR (GANZ i = 0; i < 5; i = i + 1) {
    DRUCKE("Aktueller Wert von i: " + i);
  }
  SOLANGE (zahl > 0) {
    DRUCKE("Zahl ist: " + zahl);
    zahl = zahl - 1;
  }
  DRUCKE("Test abgeschlossen.");
  ZURÜCK 0;
}
```

---

## 6. Funktionsdefinition mit Parametern und Rückgabewert
```gerlang
GANZ summe(a: GANZ, b: GANZ) {
  ZURÜCK a + b;
}
```

---

## 7. Rekursive Funktion
```gerlang
GANZ fak(n: GANZ) {
  WENN (n <= 1) {
    ZURÜCK 1;
  }
  ZURÜCK n * fak(n - 1);
}
```

---

## 8. Fehlerbehandlung
```gerlang
NIX beispiel() {
  VERSUCHE() {
    GANZ x = 5 / 0;
  } FANGE fehler {
    DRUCKE("Fehler: " + fehler);
  }
}
```

---

## 9. Benutzereingabe
```gerlang
WORT name = LESE();
DRUCKE("Hallo, " + name);
```

---

## 10. Arrays (KISTE)
```gerlang
KISTE zahlen = [1, 2, 3];
DRUCKE(zahlen[1]); // Gibt 2 aus
```

---

Weitere Beispiele findest du im Ordner `examples/`.
