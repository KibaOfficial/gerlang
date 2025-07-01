# 🛡️ GerLang – Fehlerbehandlung

> GerLang bietet eine **TypeScript-Style Fehlerbehandlung** mit präzisen Fehlermeldungen, Call-Stack-Tracking und robuster Try-Catch-Mechanik.

---

## ✨ Highlights der Fehlerbehandlung

### 🎯 TypeScript-Style Fehlermeldungen ✅ VOLLSTÄNDIG IMPLEMENTIERT
- **Präzise Positionsangaben** (Zeile:Spalte) für ALLE Runtime-Fehler
- **Farbige Ausgabe** mit Quellcode-Kontext und Caret-Zeiger (^)
- **Error-Codes** (GL001, GL002, etc.) für bessere Kategorisierung
- **Hilfreiche Tipps** für häufige Fehler und deren Behebung
- **Call-Stack** mit korrekten Funktionsaufrufreihenfolge-Positionen
- **Vollständige AST-Position-Tracking** in allen Expression-Typen

### Beispiel einer professionellen Fehlermeldung:
```
Fehler GL006: Division durch Null
  --> test.gerl:6:14
   |
  5 |     GANZ b = 0;
  6 |     ZURÜCK a / b;  // Division durch Null
   |              ^
  7 | }
   |
   Division oder Modulo durch Null ist nicht erlaubt
   = Tipp: Prüfe den Divisor vor der Operation

Call-Stack:
  0: test_division() at test.gerl:15:32
  1: haupt() at test.gerl:20:15
```

---

## 🔧 Try-Catch Mechanik (VERSUCHE/FANGE)

### Grundsyntax
```gerlang
VERSUCHE() {
    // Code, der fehlschlagen könnte
} FANGE fehler {
    // Fehlerbehandlung
    DRUCKE("Fehler abgefangen: " + fehler);
}
```

### Praktische Beispiele

#### Division durch Null abfangen
```gerlang
GANZ sichere_division(a: GANZ, b: GANZ) {
    VERSUCHE() {
        WENN (b == 0) {
            MECKER("Division durch Null nicht erlaubt!");
        }
        ZURÜCK a / b;
    } FANGE fehler {
        DRUCKE("⚠️  Fehler bei Division: " + fehler);
        ZURÜCK 0;  // Sicherer Standardwert
    }
}

GANZ haupt() {
    DRUCKE("10 / 2 = " + sichere_division(10, 2));    // 5
    DRUCKE("10 / 0 = " + sichere_division(10, 0));    // 0 (mit Fehlermeldung)
    ZURÜCK 0;
}
```

#### Array-Zugriff absichern
```gerlang
GANZ sicherer_array_zugriff(arr: KISTE, index: GANZ) {
    VERSUCHE() {
        ZURÜCK arr[index];
    } FANGE fehler {
        DRUCKE("🚫 Ungültiger Array-Index " + index + ": " + fehler);
        ZURÜCK -1;  // Fehlerindikator
    }
}

GANZ haupt() {
    KISTE zahlen = [10, 20, 30];
    
    // Gültiger Zugriff
    GANZ wert1 = sicherer_array_zugriff(zahlen, 1);   // 20
    
    // Ungültiger Zugriff (wird abgefangen)
    GANZ wert2 = sicherer_array_zugriff(zahlen, 10);  // -1 + Fehlermeldung
    
    ZURÜCK 0;
}
```

#### Benutzereingabe validieren
```gerlang
GANZ zahl_einlesen(prompt: WORT) {
    SOLANGE (JA) {
        WORT eingabe = LESE(prompt);
        
        VERSUCHE() {
            GANZ zahl = ZU_ZAHL(eingabe);  // Konvertierung kann fehlschlagen
            ZURÜCK zahl;
        } FANGE fehler {
            DRUCKE("❌ '" + eingabe + "' ist keine gültige Zahl. Bitte erneut versuchen.");
        }
    }
}

GANZ haupt() {
    GANZ alter = zahl_einlesen("Wie alt bist du? ");
    DRUCKE("Du bist " + alter + " Jahre alt.");
    ZURÜCK 0;
}
```

---

## 🎯 Error-Codes & Kategorien

GerLang verwendet ein strukturiertes Error-Code-System:

| Code   | Kategorie              | Beispiel                    |
|--------|------------------------|----------------------------|
| GL001  | Syntax-Fehler          | Fehlende Klammer           |
| GL002  | Parser-Fehler          | Ungültige Token-Folge      |
| GL003  | Undefinierte Variable  | `unbekannte_var`           |
| GL004  | Undefinierte Funktion  | `unbekannte_funktion()`    |
| GL005  | Typ-Fehler             | String + Zahl              |
| GL006  | Division durch Null    | `x / 0`                    |
| GL007  | Array-Index-Fehler     | `arr[999]`                 |
| GL008  | Import-Fehler          | Modul nicht gefunden       |
| GL009  | Export-Fehler          | Name nicht exportiert      |
| GL999  | Unbekannter Fehler     | Sonstige Runtime-Fehler    |

---

## 🔍 Debugging & Call-Stack

### Call-Stack verstehen
```gerlang
GANZ funktion_a() {
    ZURÜCK funktion_b();
}

GANZ funktion_b() {
    ZURÜCK funktion_c();
}

GANZ funktion_c() {
    ZURÜCK 10 / 0;  // Fehler hier!
}

GANZ haupt() {
    VERSUCHE() {
        GANZ result = funktion_a();
    } FANGE fehler {
        DRUCKE("Fehler im Call-Stack abgefangen!");
    }
    ZURÜCK 0;
}
```

**Call-Stack Ausgabe:**
```
Call-Stack:
  0: funktion_c() at main.gerl:12:14
  1: funktion_b() at main.gerl:8:15
  2: funktion_a() at main.gerl:4:15
  3: haupt() at main.gerl:17:23
```

---

## 💡 Best Practices

### ✅ Do's
```gerlang
// ✅ Spezifische Fehlerbehandlung
VERSUCHE() {
    GANZ result = risikanter_code();
    verarbeite_result(result);
} FANGE fehler {
    log_fehler("Spezifischer Kontext", fehler);
    // Angemessene Wiederherstellung
}

// ✅ Eingabe-Validierung
GANZ validiere_alter(alter: GANZ) {
    WENN (alter < 0 ODER alter > 150) {
        MECKER("Alter muss zwischen 0 und 150 liegen!");
    }
    ZURÜCK alter;
}

// ✅ Defensive Programmierung
GANZ sichere_funktion(arr: KISTE, index: GANZ) {
    WENN (arr.LÄNGE == 0) {
        MECKER("Array ist leer!");
    }
    WENN (index < 0 ODER index >= arr.LÄNGE) {
        MECKER("Index außerhalb der Array-Grenzen!");
    }
    ZURÜCK arr[index];
}
```

### ❌ Don'ts
```gerlang
// ❌ Fehler einfach ignorieren
VERSUCHE() {
    kritischer_code();
} FANGE fehler {
    // Schweigend ignorieren ist schlecht!
}

// ❌ Zu breite Fehlerbehandlung
VERSUCHE() {
    GANZ x = berechnung1();
    GANZ y = berechnung2();
    GANZ z = berechnung3();
    // Welche Berechnung ist fehlgeschlagen?
} FANGE fehler {
    DRUCKE("Irgendwas ist schiefgelaufen...");  // Nicht hilfreich!
}
```

---

## 🚀 Erweiterte Techniken

### Eigene Error-Funktionen
```gerlang
NIX assert(bedingung: JAIN, nachricht: WORT) {
    WENN (NICHT bedingung) {
        MECKER("Assertion failed: " + nachricht);
    }
}

NIX require_positive(wert: GANZ, name: WORT) {
    WENN (wert <= 0) {
        MECKER(name + " muss positiv sein, aber war: " + wert);
    }
}

GANZ berechne_quadratwurzel(x: GANZ) {
    require_positive(x, "Eingabewert für Quadratwurzel");
    
    // Vereinfachte Implementierung
    GANZ result = 1;
    SOLANGE (result * result < x) {
        result = result + 1;
    }
    ZURÜCK result;
}
```

### Ressourcen-Management
```gerlang
NIX datei_verarbeiten(dateiname: WORT) {
    VERSUCHE() {
        // Datei öffnen (hypothetisch)
        DATEI f = ÖFFNE(dateiname);
        
        // Verarbeitung
        WORT inhalt = f.LESE_ALLES();
        verarbeite_inhalt(inhalt);
        
        // Ressourcen freigeben
        f.SCHLIESSE();
        
    } FANGE fehler {
        DRUCKE("Fehler beim Verarbeiten von '" + dateiname + "': " + fehler);
        // Cleanup im Fehlerfall
    }
}
```

---

## 📊 Fehlerstatistiken & Monitoring

### Einfaches Error-Logging
```gerlang
GANZ fehler_counter = 0;

NIX log_fehler(kontext: WORT, fehler: WORT) {
    fehler_counter = fehler_counter + 1;
    DRUCKE("[FEHLER #" + fehler_counter + "] " + kontext + ": " + fehler);
    
    // In produktiven Systemen: In Datei schreiben
}

GANZ haupt() {
    DRUCKE("=== Programm gestartet ===");
    
    // Verschiedene Operationen mit Fehlerbehandlung
    VERSUCHE() {
        riskante_operation_1();
    } FANGE fehler {
        log_fehler("Operation 1", fehler);
    }
    
    VERSUCHE() {
        riskante_operation_2();
    } FANGE fehler {
        log_fehler("Operation 2", fehler);
    }
    
    DRUCKE("=== Programm beendet, " + fehler_counter + " Fehler aufgetreten ===");
    ZURÜCK 0;
}
```

---

## 🆘 Häufige Fehlerquellen & Lösungen

### Runtime-Fehler
| Fehler | Ursache | Lösung |
|--------|---------|---------|
| Division durch Null | `x / 0` | Divisor vorher prüfen |
| Array-Index außerhalb | `arr[999]` | Index gegen `arr.LÄNGE` prüfen |
| Undefinierte Variable | `unbekannte_var` | Variable vorher deklarieren |
| Falsche Parameterzahl | `func(1, 2, 3)` statt `func(1, 2)` | Funktionsaufruf prüfen |

### Syntax-Fehler (zur Compile-Zeit)
| Fehler | Ursache | Lösung |
|--------|---------|---------|
| Fehlende Klammer | `WENN (x > 0 {` | `WENN (x > 0) {` |
| Fehlendes Semikolon | `GANZ x = 5` | `GANZ x = 5;` |
| Ungültige Tokens | `GANZ 123abc = 5;` | `GANZ abc123 = 5;` |

---

## 🔗 Weiterführende Themen

- 📖 [Debugging-Strategien](debugging.md)
- 🔧 [Unit-Tests schreiben](testing.md)
- 💡 [Praktische Beispiele](BEISPIELE.md)
- ❓ [FAQ & Troubleshooting](faq.md)

---

**Mit GerLangs robuster Fehlerbehandlung schreibst du sichere und wartbare Programme! 🛡️**
