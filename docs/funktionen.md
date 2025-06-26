# GerLang – Funktionen

## Definition
- Syntax: `RÜCKGABETYP funktionsname(parameter: TYP, ...) { ... }`
- Rückgabe mit `ZURÜCK wert;`

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
```

---

Weitere Hinweise und Beispiele findest du in den Beispielprogrammen.
