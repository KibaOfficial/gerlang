# 📦 GerLang Modulsystem: Import & Export

> Das **GerLang Modulsystem** ermöglicht die Strukturierung großer Programme in wiederverwendbare Module mit klarer Import/Export-Syntax.

---

## ✨ Überblick

### 🎯 Warum Module?
- **Wiederverwertbarkeit:** Code einmal schreiben, überall nutzen
- **Organisation:** Große Projekte in überschaubare Teile aufteilen
- **Namensräume:** Konflikte bei Funktions-/Variablennamen vermeiden
- **Teamarbeit:** Verschiedene Entwickler arbeiten an verschiedenen Modulen

### 🔧 Grundprinzipien
- **Explizit:** Nur explizit exportierte Namen sind verfügbar
- **Sicher:** Keine versehentlichen Exporten
- **Flexibel:** Verschiedene Export-Methoden
- **Übersichtlich:** Klare Import/Export-Syntax

---

## 📤 Export von Funktionen und Variablen

### 1. Direkt-Export (bei Definition)
Exportiere Funktionen und Variablen direkt bei ihrer Definition:

```gerlang
// math_utils.gerl - Mathematik-Hilfsfunktionen

// Direkt-Export einer Funktion
GIBFREI GANZ addiere(a: GANZ, b: GANZ) {
    ZURÜCK a + b;
}

GIBFREI GANZ multipliziere(a: GANZ, b: GANZ) {
    ZURÜCK a * b;
}

// Direkt-Export einer Konstante
GIBFREI KOMMA PI = 3.14159265359;
GIBFREI GANZ MAX_WERT = 999999;

// Private Hilfsfunktion (nicht exportiert)
GANZ interne_berechnung(x: GANZ) {
    ZURÜCK x * x + 1;
}
```

### 2. Export-Liste (nachträgliche Freigabe)
Definiere Funktionen normal und exportiere sie später:

```gerlang
// string_utils.gerl - String-Hilfsfunktionen

// Normale Definitionen
GANZ zähle_wörter(text: WORT) {
    // Vereinfachte Implementierung
    GANZ anzahl = 1;
    FÜR (GANZ i = 0; i < text.LÄNGE; i = i + 1) {
        WENN (text[i] == " ") {
            anzahl = anzahl + 1;
        }
    }
    ZURÜCK anzahl;
}

WORT grossbuchstaben(text: WORT) {
    // Vereinfachte Implementierung
    ZURÜCK text;  // TODO: Implementierung
}

JAIN ist_leer(text: WORT) {
    ZURÜCK text.LÄNGE == 0;
}

// Private Hilfsfunktion
GANZ interne_string_verarbeitung(text: WORT) {
    ZURÜCK text.LÄNGE * 2;
}

// Export-Liste am Ende
GIBFREI zähle_wörter, grossbuchstaben, ist_leer;
```

### 3. Gemischter Export
Kombiniere beide Methoden nach Bedarf:

```gerlang
// game_engine.gerl - Spiel-Engine

// Direkt-Export wichtiger Konstanten
GIBFREI GANZ BILDSCHIRM_BREITE = 800;
GIBFREI GANZ BILDSCHIRM_HÖHE = 600;
GIBFREI WORT VERSION = "1.0.0";

// Normale Definitionen
JAIN spiel_läuft = JA;

NIX initialisiere_spiel() {
    DRUCKE("Spiel wird initialisiert...");
    spiel_läuft = JA;
}

NIX beende_spiel() {
    DRUCKE("Spiel wird beendet...");
    spiel_läuft = NEIN;
}

// Nachträglicher Export
GIBFREI initialisiere_spiel, beende_spiel, spiel_läuft;
```

---

## 📥 Import von Funktionen und Variablen

### Grundsyntax
```gerlang
HOLE name1, name2, name3 VON "modulname.gerl";
```

### Einfacher Import
```gerlang
// main.gerl - Hauptprogramm
HOLE addiere, PI VON "math_utils.gerl";

GANZ haupt() {
    GANZ summe = addiere(5, 3);          // 8
    DRUCKE("Summe: " + summe);
    DRUCKE("PI: " + PI);                 // 3.14159265359
    ZURÜCK 0;
}
```

### Multiple Imports
```gerlang
// calculator.gerl - Taschenrechner
HOLE addiere, multipliziere, PI VON "math_utils.gerl";
HOLE zähle_wörter, ist_leer VON "string_utils.gerl";
HOLE BILDSCHIRM_BREITE, initialisiere_spiel VON "game_engine.gerl";

GANZ haupt() {
    // Mathematik verwenden
    GANZ result = multipliziere(addiere(2, 3), 4);  // (2+3)*4 = 20
    
    // String-Verarbeitung
    WORT text = "Hallo Welt Programmierung";
    GANZ wörter = zähle_wörter(text);               // 3
    
    // Spiel-Engine
    DRUCKE("Bildschirmbreite: " + BILDSCHIRM_BREITE);
    initialisiere_spiel();
    
    DRUCKE("Rechnung: " + result);
    DRUCKE("Wörter: " + wörter);
    ZURÜCK 0;
}
```

---

## 🏗️ Praktische Module-Beispiele

### Beispiel 1: Mathe-Bibliothek
```gerlang
// math_lib.gerl - Erweiterte Mathematik-Bibliothek

// Konstanten
GIBFREI KOMMA PI = 3.14159265359;
GIBFREI KOMMA E = 2.71828182846;

// Grundrechenarten
GIBFREI GANZ addiere(a: GANZ, b: GANZ) {
    ZURÜCK a + b;
}

GIBFREI GANZ subtrahiere(a: GANZ, b: GANZ) {
    ZURÜCK a - b;
}

// Erweiterte Funktionen
GANZ potenz(basis: GANZ, exponent: GANZ) {
    GANZ result = 1;
    FÜR (GANZ i = 0; i < exponent; i = i + 1) {
        result = result * basis;
    }
    ZURÜCK result;
}

GANZ fakultät(n: GANZ) {
    WENN (n <= 1) {
        ZURÜCK 1;
    }
    ZURÜCK n * fakultät(n - 1);
}

GANZ gcd(a: GANZ, b: GANZ) {
    SOLANGE (b != 0) {
        GANZ temp = b;
        b = a % b;
        a = temp;
    }
    ZURÜCK a;
}

// Export der erweiterten Funktionen
GIBFREI potenz, fakultät, gcd;
```

### Beispiel 2: Datenstrukturen-Modul
```gerlang
// data_structures.gerl - Datenstrukturen und Algorithmen

// Stack-Implementation mit Array
KISTE stack = [];

NIX stack_push(wert: GANZ) {
    stack.ERWEITERN(wert);
}

GANZ stack_pop() {
    WENN (stack.LÄNGE == 0) {
        MECKER("Stack ist leer!");
    }
    GANZ wert = stack[stack.LÄNGE - 1];
    // TODO: Element entfernen (simplified)
    ZURÜCK wert;
}

JAIN stack_ist_leer() {
    ZURÜCK stack.LÄNGE == 0;
}

// Sortieralgorithmen
NIX bubble_sort(arr: KISTE) {
    GANZ n = arr.LÄNGE;
    FÜR (GANZ i = 0; i < n - 1; i = i + 1) {
        FÜR (GANZ j = 0; j < n - i - 1; j = j + 1) {
            WENN (arr[j] > arr[j + 1]) {
                GANZ temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

// Suchfunktionen
GANZ linear_search(arr: KISTE, ziel: GANZ) {
    FÜR (GANZ i = 0; i < arr.LÄNGE; i = i + 1) {
        WENN (arr[i] == ziel) {
            ZURÜCK i;
        }
    }
    ZURÜCK -1;  // Nicht gefunden
}

GIBFREI stack_push, stack_pop, stack_ist_leer;
GIBFREI bubble_sort, linear_search;
```

### Beispiel 3: Spiel-Utilities
```gerlang
// game_utils.gerl - Spiel-Hilfsfunktionen

// Spiel-Konstanten
GIBFREI GANZ MAX_LEBEN = 100;
GIBFREI GANZ MAX_PUNKTE = 999999;

// Spieler-Status
GANZ spieler_leben = MAX_LEBEN;
GANZ spieler_punkte = 0;

// Spieler-Funktionen
NIX schaden_nehmen(schaden: GANZ) {
    spieler_leben = spieler_leben - schaden;
    WENN (spieler_leben < 0) {
        spieler_leben = 0;
    }
    DRUCKE("💔 Schaden: " + schaden + " (Leben: " + spieler_leben + ")");
}

NIX leben_heilen(heilung: GANZ) {
    spieler_leben = spieler_leben + heilung;
    WENN (spieler_leben > MAX_LEBEN) {
        spieler_leben = MAX_LEBEN;
    }
    DRUCKE("💚 Heilung: " + heilung + " (Leben: " + spieler_leben + ")");
}

NIX punkte_hinzufügen(punkte: GANZ) {
    spieler_punkte = spieler_punkte + punkte;
    WENN (spieler_punkte > MAX_PUNKTE) {
        spieler_punkte = MAX_PUNKTE;
    }
    DRUCKE("⭐ Punkte: +" + punkte + " (Total: " + spieler_punkte + ")");
}

JAIN ist_spieler_am_leben() {
    ZURÜCK spieler_leben > 0;
}

NIX zeige_status() {
    DRUCKE("=== Spieler-Status ===");
    DRUCKE("Leben: " + spieler_leben + "/" + MAX_LEBEN);
    DRUCKE("Punkte: " + spieler_punkte);
    DRUCKE("Status: " + (ist_spieler_am_leben() ? "Lebendig" : "Tot"));
}

GIBFREI schaden_nehmen, leben_heilen, punkte_hinzufügen;
GIBFREI ist_spieler_am_leben, zeige_status;
```

---

## 🎮 Komplettes Projekt-Beispiel

### main.gerl - Hauptprogramm
```gerlang
// Imports aus verschiedenen Modulen
HOLE addiere, potenz, PI VON "math_lib.gerl";
HOLE bubble_sort, linear_search VON "data_structures.gerl";
HOLE schaden_nehmen, leben_heilen, zeige_status VON "game_utils.gerl";

GANZ haupt() {
    DRUCKE("🚀 === Multi-Modul Demo ===\n");
    
    // Mathe-Bibliothek testen
    DRUCKE("📊 Mathematik:");
    GANZ summe = addiere(5, 3);
    GANZ quadrat = potenz(4, 2);
    DRUCKE("  5 + 3 = " + summe);
    DRUCKE("  4² = " + quadrat);
    DRUCKE("  π = " + PI);
    DRUCKE("");
    
    // Datenstrukturen testen
    DRUCKE("🔍 Datenstrukturen:");
    KISTE zahlen = [64, 34, 25, 12, 22, 11, 90];
    DRUCKE("  Original: " + zahlen);
    
    bubble_sort(zahlen);
    DRUCKE("  Sortiert: " + zahlen);
    
    GANZ index = linear_search(zahlen, 25);
    DRUCKE("  Index von 25: " + index);
    DRUCKE("");
    
    // Spiel-Utilities testen
    DRUCKE("🎮 Spiel-Simulation:");
    zeige_status();
    
    schaden_nehmen(30);
    leben_heilen(15);
    zeige_status();
    
    DRUCKE("\n✅ Alle Module erfolgreich getestet!");
    ZURÜCK 0;
}
```

**Ausgabe:**
```
🚀 === Multi-Modul Demo ===

📊 Mathematik:
  5 + 3 = 8
  4² = 16
  π = 3.14159265359

🔍 Datenstrukturen:
  Original: [64, 34, 25, 12, 22, 11, 90]
  Sortiert: [11, 12, 22, 25, 34, 64, 90]
  Index von 25: 3

🎮 Spiel-Simulation:
=== Spieler-Status ===
Leben: 100/100
Punkte: 0
Status: Lebendig
💔 Schaden: 30 (Leben: 70)
💚 Heilung: 15 (Leben: 85)
=== Spieler-Status ===
Leben: 85/100
Punkte: 0
Status: Lebendig

✅ Alle Module erfolgreich getestet!
```

---

## ⚠️ Wichtige Hinweise & Best Practices

### ✅ Do's
```gerlang
// ✅ Klare Modulnamen
// math_utils.gerl, string_helpers.gerl, game_engine.gerl

// ✅ Zusammengehörige Funktionen gruppieren
GIBFREI addiere, subtrahiere, multipliziere, dividiere;

// ✅ Konstanten exportieren
GIBFREI GANZ MAX_WERT = 999;
GIBFREI WORT VERSION = "1.0.0";

// ✅ Private Hilfsfunktionen nicht exportieren
GANZ interne_berechnung(x: GANZ) { ... }  // Nicht exportiert

// ✅ Dokumentation in Modulen
// math_utils.gerl - Grundlegende mathematische Operationen
// Autor: Max Mustermann
// Version: 1.2.0
```

### ❌ Don'ts
```gerlang
// ❌ Alles exportieren
GIBFREI interne_temp_variable, debug_helper, temp_func;

// ❌ Unklare Namen
HOLE f, g, h VON "utils.gerl";

// ❌ Zu große Module (> 200 Zeilen)
// Teile große Module in kleinere auf

// ❌ Zirkuläre Abhängigkeiten
// modul_a.gerl importiert von modul_b.gerl
// modul_b.gerl importiert von modul_a.gerl  // Problematisch!
```

### 🔧 Fehlerbehandlung
```gerlang
// Modul nicht gefunden
HOLE unbekannte_funktion VON "nicht_existiert.gerl";
// Fehler: Modul 'nicht_existiert.gerl' nicht gefunden

// Name nicht exportiert
HOLE private_funktion VON "math_utils.gerl";
// Fehler: 'private_funktion' ist nicht in 'math_utils.gerl' exportiert

// Typfehler beim Import
HOLE addiere VON "math_utils.gerl";
WORT result = addiere(1, 2);  // Fehler: addiere() gibt GANZ zurück
```

---

## 📁 Projektstruktur-Empfehlungen

```
mein_projekt/
├── main.gerl              // Hauptprogramm
├── lib/                   // Bibliotheken
│   ├── math_utils.gerl
│   ├── string_helpers.gerl
│   └── data_structures.gerl
├── game/                  // Spiel-spezifische Module
│   ├── player.gerl
│   ├── enemies.gerl
│   └── levels.gerl
└── tests/                 // Test-Dateien
    ├── test_math.gerl
    └── test_game.gerl
```

---

## 🚀 Weiterführende Themen

- 🔧 [Funktionen & Parameter](funktionen.md)
- 📊 [Arrays & Datenstrukturen](arrays.md)
- 🛡️ [Fehlerbehandlung](fehlerbehandlung.md)
- 💡 [Praktische Beispiele](BEISPIELE.md)
- ❓ [FAQ & Troubleshooting](faq.md)

---

**Mit dem GerLang Modulsystem baust du saubere, wartbare und wiederverwendbare Programme! 📦**
