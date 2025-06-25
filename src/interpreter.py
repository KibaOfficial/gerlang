# Copyright (c) 2025 KibaOfficial
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from parser import (
    Program, FunctionDeclaration, IfStatement, WhileStatement, ForStatement, BlockStatement, ReturnStatement,
    ExpressionStatement, VariableDeclaration, Expression, CallExpression, IdentifierExpression, LiteralExpression,
    BinaryExpression, UnaryExpression, AssignmentStatement, PrintStatement
)

class Environment:
    def __init__(self, parent=None):
        self.vars = {}
        self.parent = parent

    def define(self, name, value):
        self.vars[name] = value

    def assign(self, name, value):
        if name in self.vars:
            self.vars[name] = value
        elif self.parent:
            self.parent.assign(name, value)
        else:
            raise Exception(f"Variable '{name}' nicht definiert")

    def get(self, name):
        if name in self.vars:
            return self.vars[name]
        elif self.parent:
            return self.parent.get(name)
        else:
            raise Exception(f"Variable '{name}' nicht definiert")

class ReturnSignal(Exception):
    def __init__(self, value):
        self.value = value

class Interpreter:
    def __init__(self):
        self.globals = Environment()
        self.env = self.globals
        self.functions = {}

        # Builtins definieren
        self.setup_builtins()

    def setup_builtins(self):
        """Definiert alle eingebauten Funktionen"""
        # DRUCKE/ZEIGE für Output
        self.globals.define("DRUCKE", self._drucke_builtin)
        self.globals.define("ZEIGE", self._drucke_builtin)

        # LESE für Input
        self.globals.define("LESE", self._lese_builtin)

        # Type conversion functions
        self.globals.define("WORT", self._zu_wort)
        self.globals.define("GANZ", self._zu_ganz)
        self.globals.define("KOMMA", self._zu_komma)

    def interpret(self, program: Program):
        """Interpretiert das gesamte Programm"""
        # Erst alle Funktionen sammeln
        for stmt in program.statements:
            if isinstance(stmt, FunctionDeclaration):
                self.functions[stmt.name] = stmt

        # Dann alle globalen Statements ausführen (außer Funktionen)
        for stmt in program.statements:
            if not isinstance(stmt, FunctionDeclaration):
                self.execute(stmt)

        # Falls HAUPT vorhanden ist, diese ausführen
        if "haupt" in self.functions:
            return self.execute_function("haupt", [])

        return None

    def execute_function(self, name, args):
        """Führt eine Funktion aus"""
        func = self.functions.get(name)
        if not func:
            raise Exception(f"Funktion '{name}' nicht gefunden.")

        # Parameter-Anzahl prüfen
        if len(args) != len(func.parameters):
            raise Exception(f"Funktion '{name}' erwartet {len(func.parameters)} Argumente, {len(args)} gegeben")

        # Neue lokale Umgebung erstellen
        local_env = Environment(self.globals)

        # Parameter binden
        for (ptype, pname), arg in zip(func.parameters, args):
            local_env.define(pname, arg)

        # Umgebung wechseln
        previous_env = self.env
        self.env = local_env

        try:
            self.execute(func.body)
            # Kein explizites Return -> None zurückgeben
            return None
        except ReturnSignal as r:
            return r.value
        finally:
            # Umgebung immer wiederherstellen
            self.env = previous_env

    def execute(self, stmt):
        """Führt ein Statement aus"""
        if isinstance(stmt, BlockStatement):
            # Neue Scope für Block erstellen
            block_env = Environment(self.env)
            previous_env = self.env
            self.env = block_env

            try:
                for s in stmt.statements:
                    self.execute(s)
            finally:
                self.env = previous_env

        elif isinstance(stmt, ExpressionStatement):
            self.evaluate(stmt.expression)

        elif isinstance(stmt, VariableDeclaration):
            value = self.evaluate(stmt.initializer) if stmt.initializer else None
            self.env.define(stmt.name, value)

        elif isinstance(stmt, AssignmentStatement):
            value = self.evaluate(stmt.value)
            self.env.assign(stmt.name, value)

        elif isinstance(stmt, IfStatement):
            cond = self.evaluate(stmt.condition)
            if self.is_truthy(cond):
                self.execute(stmt.then_branch)
            elif stmt.else_branch:
                self.execute(stmt.else_branch)

        elif isinstance(stmt, WhileStatement):
            while self.is_truthy(self.evaluate(stmt.condition)):
                self.execute(stmt.body)

        elif isinstance(stmt, ForStatement):
            # For-Loop Scope
            for_env = Environment(self.env)
            previous_env = self.env
            self.env = for_env

            try:
                # Initializer
                if stmt.initializer:
                    self.execute(stmt.initializer)

                # Loop
                while True:
                    # Condition check
                    if stmt.condition and not self.is_truthy(self.evaluate(stmt.condition)):
                        break

                    # Body ausführen
                    self.execute(stmt.body)

                    # Increment
                    if stmt.increment:
                        # Kann AssignmentStatement oder ExpressionStatement sein
                        if isinstance(stmt.increment, (AssignmentStatement, ExpressionStatement)):
                            self.execute(stmt.increment)
                        else:
                            self.evaluate(stmt.increment)
            finally:
                self.env = previous_env

        elif isinstance(stmt, ReturnStatement):
            value = self.evaluate(stmt.value) if stmt.value else None
            raise ReturnSignal(value)

        elif isinstance(stmt, PrintStatement):
            value = self.evaluate(stmt.expression)
            print(value)

        else:
            raise Exception(f"Unbekanntes Statement: {type(stmt)}")

    def evaluate(self, expr):
        """Evaluiert einen Ausdruck"""
        if isinstance(expr, LiteralExpression):
            return expr.value

        elif isinstance(expr, IdentifierExpression):
            return self.env.get(expr.name)

        elif isinstance(expr, BinaryExpression):
            left = self.evaluate(expr.left)
            right = self.evaluate(expr.right)

            # Arithmetische Operatoren
            if expr.operator in ("+", "PLUS"):
                # Automatisches String-Concatenation
                if isinstance(left, str) or isinstance(right, str):
                    return str(left) + str(right)
                return left + right
            elif expr.operator in ("-", "MINUS"):
                return left - right
            elif expr.operator in ("*", "MULTIPLY"):
                return left * right
            elif expr.operator in ("/", "DIVIDE"):
                if right == 0:
                    raise Exception("Division durch Null")
                return left / right
            elif expr.operator in ("%", "MODULO"):
                return left % right

            # Vergleichsoperatoren
            elif expr.operator in ("==", "GLEICH"):
                return left == right
            elif expr.operator in ("!=", "UNGLEICH"):
                return left != right
            elif expr.operator in ("<", "LT"):
                return left < right
            elif expr.operator in ("<="):
                return left <= right
            elif expr.operator in (">", "GT"):
                return left > right
            elif expr.operator in (">="):
                return left >= right

            # Logische Operatoren
            elif expr.operator in ("&&", "UND"):
                return self.is_truthy(left) and self.is_truthy(right)
            elif expr.operator in ("||", "ODER"):
                return self.is_truthy(left) or self.is_truthy(right)

            else:
                raise Exception(f"Unbekannter binärer Operator: {expr.operator}")

        elif isinstance(expr, UnaryExpression):
            operand = self.evaluate(expr.operand)

            if expr.operator in ("-", "MINUS"):
                return -operand
            elif expr.operator in ("!", "NOT", "NICHT"):
                return not self.is_truthy(operand)
            else:
                raise Exception(f"Unbekannter unärer Operator: {expr.operator}")

        elif isinstance(expr, CallExpression):
            # Funktion evaluieren
            if isinstance(expr.function, IdentifierExpression):
                func_name = expr.function.name

                # Erst in Builtins suchen
                try:
                    func = self.env.get(func_name)
                    if callable(func):
                        args = [self.evaluate(arg) for arg in expr.arguments]
                        return func(*args)
                except Exception:
                    pass

                # Dann in benutzerdefinierten Funktionen
                if func_name in self.functions:
                    args = [self.evaluate(arg) for arg in expr.arguments]
                    return self.execute_function(func_name, args)

                raise Exception(f"Unbekannte Funktion: {func_name}")
            else:
                # Komplexerer Funktionsausdruck
                func = self.evaluate(expr.function)
                if callable(func):
                    args = [self.evaluate(arg) for arg in expr.arguments]
                    return func(*args)
                else:
                    raise Exception("Ausdruck ist nicht aufrufbar")

        else:
            raise Exception(f"Unbekannter Ausdruck: {type(expr)}")

    def is_truthy(self, value):
        """Bestimmt ob ein Wert als wahr betrachtet wird"""
        if value is None:
            return False
        if isinstance(value, bool):
            return value
        if isinstance(value, (int, float)):
            return value != 0
        if isinstance(value, str):
            return len(value) > 0
        return True

    # === BUILTIN FUNKTIONEN ===

    def _drucke_builtin(self, *args):
        """DRUCKE/ZEIGE - Ausgabe auf Konsole"""
        output = " ".join(str(arg) for arg in args)
        print(output)
        return None

    def _lese_builtin(self, prompt=""):
        """LESE - Eingabe von Konsole"""
        if prompt:
            return input(str(prompt))
        return input()

    def _zu_wort(self, value):
        """Konvertiert zu String"""
        return str(value)

    def _zu_ganz(self, value):
        """Konvertiert zu Integer"""
        try:
            if isinstance(value, str):
                return int(float(value))  # Erst float für "42.0" -> 42
            return int(value)
        except (ValueError, TypeError):
            raise Exception(f"Kann '{value}' nicht zu GANZ konvertieren")

    def _zu_komma(self, value):
        """Konvertiert zu Float"""
        try:
            return float(value)
        except (ValueError, TypeError):
            raise Exception(f"Kann '{value}' nicht zu KOMMA konvertieren")