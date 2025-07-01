# 💬 GerLang – Ein- und Ausgabe

> **Vollständige Ein-/Ausgabe-Referenz** für GerLang mit interaktiver Benutzereingabe und formatierter Ausgabe.

---

## 📤 Ausgabe

### Grundlegende Ausgabe
```gerlang
DRUCKE("Hallo Welt");              // String-Ausgabe
DRUCKE(42);                        // Zahlen-Ausgabe
DRUCKE(3.14);                      // Kommazahlen-Ausgabe
DRUCKE(JA);                        // Boolean-Ausgabe
```

### Variable und Ausdrücke ausgeben
```gerlang
GANZ zahl = 42;
WORT name = "Max";
JAIN aktiv = JA;

DRUCKE(zahl);                      // Variable ausgeben
DRUCKE(zahl + 8);                  // Ausdruck berechnen und ausgeben
DRUCKE("Name: " + name);           // String-Verkettung
```

### Arrays und komplexe Datentypen
```gerlang
KISTE zahlen = [1, 2, 3, 4, 5];
KISTE matrix = [[1, 2], [3, 4]];

DRUCKE(zahlen);                    // Ganzes Array ausgeben
DRUCKE(zahlen[0]);                 // Einzelnes Element
DRUCKE(matrix[1][0]);              // Mehrdimensionaler Zugriff
```

---

## 📥 Eingabe ✅ VOLLSTÄNDIG IMPLEMENTIERT

### Interaktive Benutzereingabe
```gerlang
// Einfache Eingabe
WORT eingabe = LESE("Bitte Namen eingeben: ");
DRUCKE("Hallo, " + eingabe + "!");

// Zahlen-Eingabe (als String, dann konvertieren)
WORT zahl_text = LESE("Bitte eine Zahl eingeben: ");
// TODO: ZU_ZAHL() Funktion für Konvertierung
```

### Eingabe in Schleifen
```gerlang
GANZ haupt() {
    WORT eingabe = "";
    
    SOLANGE (eingabe != "ende") {
        eingabe = LESE("Eingabe (oder 'ende' zum Beenden): ");
        DRUCKE("Du hast eingegeben: " + eingabe);
    }
    
    ZURÜCK 0;
}
```

---

## 🎯 Praktische Beispiele

### Interaktives Zahlenraten
```gerlang
GANZ haupt() {
    GANZ geheimzahl = 42;  // TODO: ZUFALLSZAHL() implementieren
    WORT antwort;
    
    DRUCKE("=== Zahlenraten ===");
    DRUCKE("Ich denke an eine Zahl zwischen 1 und 100!");
    
    SOLANGE (antwort != "42") {
        antwort = LESE("Dein Tipp: ");
        
        WENN (antwort == "42") {
            DRUCKE("🎉 Richtig geraten!");
        } SONST {
            DRUCKE("Leider falsch, versuch es nochmal!");
        }
    }
    
    ZURÜCK 0;
}
```

### Einfacher Taschenrechner
```gerlang
GANZ haupt() {
    DRUCKE("=== GerLang Taschenrechner ===");
    
    WORT zahl1_str = LESE("Erste Zahl: ");
    WORT operator = LESE("Operator (+, -, *, /): ");
    WORT zahl2_str = LESE("Zweite Zahl: ");
    
    // TODO: String zu Zahl Konvertierung implementieren
    // GANZ zahl1 = ZU_ZAHL(zahl1_str);
    // GANZ zahl2 = ZU_ZAHL(zahl2_str);
    
    DRUCKE("Berechnung: " + zahl1_str + " " + operator + " " + zahl2_str);
    
    ZURÜCK 0;
}
```

---

## 🚀 Status & Roadmap

### ✅ Vollständig implementiert
- **DRUCKE()**: Ausgabe aller Datentypen
- **LESE()**: Interaktive String-Eingabe mit Prompt
- **String-Verkettung**: Mit `+` Operator
- **Variable Ausgabe**: Direkte Ausgabe von Variablen und Ausdrücken

### 🔄 In Entwicklung
- **ZU_ZAHL()**: String zu Zahl Konvertierung
- **ZU_KOMMA()**: String zu Float Konvertierung  
- **FORMATIERE()**: Formatierte Ausgabe mit Platzhaltern
- **DATEI_LESE()**: Dateieingabe
- **DATEI_SCHREIBE()**: Dateiausgabe

---

**Tipp:** Die Ein-/Ausgabe-Funktionen sind vollständig funktionsfähig und können für interaktive Programme genutzt werden! 🎮
