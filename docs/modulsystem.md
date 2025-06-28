# GerLang Modulsystem: Import & Export

## Export von Funktionen und Variablen

Du kannst Funktionen und Variablen auf zwei Arten aus einem Modul exportieren:

### 1. Direkt-Export (explizite Deklaration)
```gerlang
GIBFREI GANZ addiere(a: GANZ, b: GANZ) {
  ZURÜCK a + b;
}

GIBFREI GANZ zahlB = 10;
```

### 2. Export-Liste (nachträgliche Freigabe)
```gerlang
GANZ addiere(a: GANZ, b: GANZ) {
  ZURÜCK a + b;
}
GANZ zahlB = 10;

GIBFREI addiere, zahlB;
```

Beide Varianten können beliebig kombiniert werden.

## Import von Funktionen und Variablen

Im Hauptprogramm (oder einem anderen Modul) kannst du beliebige Namen aus einem Modul importieren:

```gerlang
HOLE addiere, zahlB VON "math.gerl";

GANZ haupt() {
  GANZ a = 5;
  GANZ ergebnis = addiere(a, zahlB);
  DRUCKE("Das Ergebnis der Addition ist: " + ergebnis);
  ZURÜCK 0;
}
```

## Hinweise
- Nur Namen, die explizit exportiert wurden (egal auf welche Weise), können importiert werden.
- Die Reihenfolge der Statements im Modul ist beliebig.
- Export-Listen (`GIBFREI name1, name2;`) müssen sich auf vorher deklarierte Funktionen/Variablen beziehen.
- Import und Export funktionieren für beliebig viele Namen.

## Fehlerquellen
- Wird ein Name importiert, der nicht exportiert wurde, gibt es eine Fehlermeldung.
- Die Funktionsparameter müssen im Format `name: TYP` angegeben werden.

---
Stand: 28.06.2025
