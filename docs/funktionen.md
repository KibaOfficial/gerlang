# GerLang – Funktionen

## Definition
- Syntax: `RÜCKGABETYP funktionsname(parameter: TYP, ...) { ... }`
- Rückgabe mit `ZURÜCK wert;`
- Parameter werden als `name: TYP` angegeben, mehrere durch Komma getrennt.

Beispiel:
```gerlang
GANZ addiere(a: GANZ, b: GANZ) {
  ZURÜCK a + b;
}
```

## Parameter
- Jeder Parameter benötigt einen Typ.
- Mehrere Parameter werden durch Kommas getrennt.

## Rückgabewerte
- Rückgabewert wird mit `ZURÜCK` angegeben.
- Funktionen ohne Rückgabewert nutzen `NIX` als Typ.

## Rekursion
- Funktionen können sich selbst aufrufen.

Beispiel:
```gerlang
GANZ fakultaet(n: GANZ) {
  WENN (n < 2) {
    ZURÜCK 1;
  }
  ZURÜCK n * fakultaet(n-1);
}
GANZ haupt() {
  DRUCKE(fakultaet(5));
  ZURÜCK 0;
}
```

## Fehlerbehandlung in Funktionen
```gerlang
GANZ beispiel() {
  VERSUCHE() {
    GANZ x = 5 / 0;
  } FANGE fehler {
    DRUCKE("Fehler: " + fehler);
  }
  ZURÜCK 0;
}
```

---

Weitere Hinweise und Beispiele findest du in den Beispielprogrammen.
