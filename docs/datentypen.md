# GerLang – Datentypen

## Übersicht
GerLang unterstützt verschiedene Datentypen, die jeweils einen bestimmten Wertebereich und Zweck haben.

| Typ     | Bedeutung             | Beispiel                |
|---------|-----------------------|------------------------|
| GANZ    | Ganzzahl (int)        | GANZ x = 5;            |
| KOMMA   | Kommazahl (float)     | KOMMA pi = 3.14;       |
| WORT    | Zeichenkette (str)    | WORT name = "Max";     |
| JAIN    | Boolescher Wert       | JAIN ok = JA;          |
| KISTE   | Array/Liste           | KISTE zahlen = [1,2,3];|

## Literale
- **GANZ:** 1, -5, 42
- **KOMMA:** 3.14, -0.5
- **WORT:** "Hallo", "Test123"
- **JAIN:** JA, NEIN, VIELLEICHT (None/Null)
- **KISTE:** [1, 2, 3], ["a", "b", 3]

## Typumwandlung
- Automatische Typumwandlung ist nicht vorgesehen.
- Typen müssen explizit angegeben werden.

## Besonderheiten
- Arrays (KISTE) können beliebige Typen enthalten.
- Typisierung ist strikt.
- Fehlerbehandlung und Eingabe sind Teil der Sprache.

## Methoden für Datentypen

Viele Datentypen in GerLang besitzen eingebaute Methoden, die direkt auf Variablen angewendet werden können:

| Typ     | Methode         | Bedeutung / Beispiel                                  |
|---------|-----------------|------------------------------------------------------|
| WORT    | LÄNGE           | Gibt die Länge des Wortes zurück: `wort.LÄNGE`        |
| KISTE   | LÄNGE           | Gibt die Anzahl der Elemente zurück: `kiste.LÄNGE`    |
| KISTE   | HINZUFÜGEN(x)   | Fügt x am Anfang der Liste ein: `kiste.HINZUFÜGEN(1)` |
| KISTE   | ERWEITERN(x)    | Fügt x am Ende der Liste an: `kiste.ERWEITERN(2)`     |

**Beispiel:**
```gerlang
KISTE zahlen = [1, 2, 3];
DRUCKE(zahlen.LÄNGE);         // 3
zahlen.HINZUFÜGEN(0);
DRUCKE(zahlen);               // [0, 1, 2, 3]
zahlen.ERWEITERN(4);
DRUCKE(zahlen);               // [0, 1, 2, 3, 4]
WORT text = "Hallo Welt";
DRUCKE(text.LÄNGE);           // 10
```

Weitere Methoden können in Zukunft ergänzt werden.

---

Weitere Details und Beispiele findest du in den Kapiteln zu Variablen, Arrays und Fehlerbehandlung.
