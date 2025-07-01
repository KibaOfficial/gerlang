# ❓ GerLang – FAQ

> **Häufig gestellte Fragen** und deren Antworten zu GerLang Features, Syntax und Troubleshooting.

---

## 🚀 Grundlagen

### **Wie führe ich ein GerLang-Programm aus?**
```bash
# Python-Version
python gerlang.py run mein_programm.gerl

# EXE-Version (Windows)
./bin/gerlc.exe run mein_programm.gerl

# Mit Argumenten
python gerlang.py run programm.gerl --verbose
```

### **Welche Dateierweiterung verwendet GerLang?**
GerLang-Dateien haben die Erweiterung `.gerl` (German Language).

### **Brauche ich eine `haupt()`-Funktion?**
Ja! Jedes GerLang-Programm benötigt eine `haupt()`-Funktion:
```gerlang
GANZ haupt() {
    DRUCKE("Hallo Welt!");
    ZURÜCK 0;  // Exit-Code
}
```

---

## 💻 Sprachfeatures

### **Kann ich eigene Datentypen definieren?**
Noch nicht vollständig implementiert, aber geplant:
```gerlang
// Geplant für zukünftige Versionen
ORDNUNG Person {
    WORT name;
    GANZ alter;
}
```

### **Gibt es eine Standardbibliothek?**
Ja, mit vielen built-in Funktionen:
- **Ein-/Ausgabe**: `DRUCKE()`, `LESE()`
- **Array-Methoden**: `.LÄNGE`, `.HINZUFÜGEN()`, `.ERWEITERN()`
- **Math-Funktionen (V4.0+)**: `WURZEL()`, `POTENZ()`, `ABS()`, `RUNDEN()`, `ZUFALLSBEREICH()`
- **Typ-Konvertierung**: `ZU_WORT()`, `ZU_GANZ()`, `ZU_KOMMA()`
- **Fehlerbehandlung**: `VERSUCHE()`/`FANGE` Blöcke

### **Unterstützt GerLang String-Interpolation?**
Ja! Seit Version 4.0 gibt es moderne Template-Strings:
```gerlang
WORT name = "Max";
GANZ alter = 25;
DRUCKE("Hallo ${name}, du bist ${alter} Jahre alt!");
DRUCKE("Nächstes Jahr wirst du ${alter + 1}");
```
- **String-Methoden**: `.LÄNGE`
- **Geplant**: `WURZEL()`, `POTENZ()`, `ZUFALLSZAHL()`

### **Wie funktioniert die Fehlerbehandlung?**  
✅ **Vollständig implementiert** mit TypeScript-Style Fehlermeldungen:
```gerlang
VERSUCHE() {
    GANZ result = 10 / 0;  // Division durch Null
} FANGE fehler {
    DRUCKE("Fehler abgefangen: " + fehler);
}
```

**Beispiel-Fehlermeldung:**
```
Fehler GL006: Division durch Null
  --> test.gerl:6:14
   |
  6 |     GANZ result = 10 / 0;
   |                      ^
   |
   Division oder Modulo durch Null ist nicht erlaubt
   = Tipp: Prüfe den Divisor vor der Operation
```

---

## 📊 Datentypen & Arrays

### **Wie kann ich Arrays mit gemischten Typen nutzen?**
```gerlang
KISTE gemischt = [1, "zwei", 3.14, JA];
DRUCKE(gemischt[0]);  // 1
DRUCKE(gemischt[1]);  // "zwei"
```

### **Was ist der Unterschied zwischen GANZ und KOMMA?**
- **GANZ**: Ganzzahlen (int) → `42`, `-17`, `0`
- **KOMMA**: Kommazahlen (float) → `3.14`, `-0.5`, `2.0`

### **Wie funktionieren mehrdimensionale Arrays?**
```gerlang
KISTE matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];

GANZ wert = matrix[1][2];  // 6
matrix[0][0] = 99;         // Zuweisung
```

---

## 🔧 Module & Imports

### **Wie verwende ich das Modulsystem?**
**Exportieren (math.gerl):**
```gerlang
GIBFREI GANZ addiere(a: GANZ, b: GANZ) {
    ZURÜCK a + b;
}

GIBFREI GANZ PI = 3.14159;
```

**Importieren (main.gerl):**
```gerlang
HOLE addiere, PI VON "math.gerl";

GANZ haupt() {
    GANZ summe = addiere(5, 3);
    DRUCKE("Summe: " + summe);
    ZURÜCK 0;
}
```

---

## 🛠️ Troubleshooting

### **Warum bekomme ich "Funktion 'haupt' nicht gefunden"?**
Jedes Programm benötigt eine `haupt()`-Funktion mit `GANZ` Rückgabetyp:
```gerlang
// ❌ Falsch
NIX haupt() { ... }

// ✅ Richtig  
GANZ haupt() {
    ZURÜCK 0;
}
```

### **Wie kann ich Debugging-Informationen sehen?**
```bash
# Verbose-Modus
python gerlang.py run programm.gerl --verbose

# AST anzeigen
python gerlang.py ast programm.gerl

# Tokens anzeigen
python gerlang.py tokens programm.gerl
```

### **Warum funktioniert mein Import nicht?**
- Prüfe die Datei-Pfade (relativ zur importierenden Datei)
- Stelle sicher, dass die Funktionen/Variablen exportiert sind (`GIBFREI`)
- Verwende die korrekte Syntax: `HOLE name VON "datei.gerl";`

---

## 🎯 Performance & Limits

### **Wie schnell ist GerLang?**
GerLang ist ein **interpretierte Sprache** und daher nicht für Performance-kritische Anwendungen optimiert. Sie ist designed für:
- Lernzwecke und Prototyping
- Esoterische/experimentelle Programme
- Humorvolle Projekte mit deutscher Syntax

### **Gibt es Limits bei Rekursion/Arrays?**
- **Rekursion**: Python's Standard-Limit (~1000 Aufrufe)
- **Arrays**: Begrenzt durch verfügbaren Arbeitsspeicher
- **Strings**: Praktisch unbegrenzt

---

## 🆘 Weitere Hilfe

### **Wo finde ich mehr Beispiele?**
- 📁 `examples/` - Offizielle Beispielprogramme
- 📖 `docs/BEISPIELE.md` - Detaillierte Code-Beispiele
- 📚 `docs/SPRACHE.md` - Vollständige Sprachreferenz

### **Wie kann ich zur Entwicklung beitragen?**
1. Issues auf GitHub erstellen
2. Pull Requests mit Verbesserungen
3. Neue Beispielprogramme beisteuern
4. Dokumentation verbessern

### **Wo bekomme ich Support?**
- 📖 Dokumentation in `docs/`
- 🐛 GitHub Issues für Bugs
- 💡 GitHub Discussions für Feature-Requests

---

**GerLang macht Programmieren auf Deutsch möglich! 🇩🇪** 🚀
