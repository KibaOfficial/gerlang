# 📝 GerLang – Syntax-Referenz

> **Vollständige Syntax-Referenz** für GerLang mit modernen Sprachfeatures, Methoden-System und Best Practices.

---

## 📋 Inhaltsverzeichnis
1. [Grundlegende Syntax](#grundlegende-syntax)
2. [Anweisungen & Blöcke](#anweisungen--blöcke)
3. [Kommentare](#kommentare)
4. [Methoden-System](#methoden-system)
5. [Namenskonventionen](#namenskonventionen)
6. [Best Practices](#best-practices)

---

## Grundlegende Syntax

### Struktur & Formatierung
- **Anweisungen** enden mit Semikolon (`;`)
- **Blöcke** werden mit `{ ... }` geklammert
- **Einrückung** wird empfohlen (2 oder 4 Leerzeichen)
- **Case-Sensitivity**: GerLang unterscheidet Groß-/Kleinschreibung

```gerlang
GANZ haupt() {
    GANZ x = 5;        // Anweisung mit Semikolon
    DRUCKE(x);         // Funktionsaufruf
    ZURÜCK 0;          // Rückgabe mit Semikolon
}
```

## Anweisungen & Blöcke

### Einfache Anweisungen
```gerlang
GANZ zahl = 42;                    // Variablendeklaration
zahl = zahl + 1;                   // Zuweisung
DRUCKE("Hallo Welt");             // Funktionsaufruf
```

### Blöcke und Scope
```gerlang
{   // Block-Anfang
    GANZ lokale_variable = 10;     // Nur in diesem Block sichtbar
    DRUCKE(lokale_variable);
}   // Block-Ende - lokale_variable nicht mehr verfügbar
```

### Komplexe Ausdrücke & Zuweisungen
```gerlang
// Array-Element Zuweisungen
KISTE zahlen = [1, 2, 3];
zahlen[0] = 99;                    // Einfacher Array-Zugriff

// Mehrdimensionale Arrays
KISTE matrix = [[1, 2], [3, 4]];
matrix[0][1] = 42;                 // Verschachtelte Zugriffe

// Methoden-Aufrufe
zahlen.ERWEITERN(4);               // Methode auf Array
GANZ länge = zahlen.LÄNGE;         // Property-Zugriff
```

## Kommentare

### Einzeilige Kommentare
```gerlang
// Standard-Kommentar
GANZ x = 5;  // Kommentar am Zeilenende

HINWEIS: Alternative Kommentar-Syntax
GANZ y = 10;  HINWEIS: Auch am Zeilenende möglich
```

### Kommentar-Best-Practices
```gerlang
// ✅ Gut: Erklärt WARUM, nicht WAS
// Verwende Faktor 2 für bessere Performance
GANZ result = eingabe * 2;

// ❌ Schlecht: Erklärt nur WAS der Code tut
// Multipliziere eingabe mit 2
GANZ result = eingabe * 2;
```

## Methoden-System

### String-Methoden (WORT)
```gerlang
WORT text = "Hallo Welt";
GANZ länge = text.LÄNGE;           // Property: Länge ermitteln
```

### Array-Methoden (KISTE)
```gerlang
KISTE liste = [1, 2, 3];
GANZ anzahl = liste.LÄNGE;         // Property: Anzahl Elemente

liste.HINZUFÜGEN(0);               // Methode: Am Anfang einfügen
liste.ERWEITERN(4);                // Methode: Am Ende anhängen

// Chainable Operations möglich
KISTE neue_liste = [1, 2];
neue_liste.ERWEITERN(3).ERWEITERN(4);  // Noch nicht implementiert
```

### Methoden-Aufruf Syntax
```gerlang
objekt.METHODE(parameter1, parameter2);     // Mit Parametern
objekt.PROPERTY;                            // Property-Zugriff ohne ()
```

## Namenskonventionen
- Variablen- und Funktionsnamen sollten beschreibend und klein geschrieben werden (z.B. `anzahl`, `berechne_summe`).
- Keine Sonderzeichen außer `_` erlaubt.

## Best Practices
- Kommentare nutzen, um Code verständlich zu machen.
- Blöcke und Einrückungen übersichtlich gestalten.
- Aussagekräftige Namen verwenden.

---

Weitere Beispiele und Hinweise findest du in den anderen Dokumentationsdateien.
