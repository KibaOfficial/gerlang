# Copyright (c) 2025 KibaOfficial
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import os
import math
import random
from parser import (
    Program, FunctionDeclaration, IfStatement, WhileStatement, ForStatement, BlockStatement, ReturnStatement,
    ExpressionStatement, VariableDeclaration, Expression, CallExpression, IdentifierExpression, LiteralExpression,
    BinaryExpression, UnaryExpression, AssignmentStatement, PrintStatement,
    ArrayLiteralExpression, ArrayAccessExpression, TryCatchStatement, PropertyAccessExpression, MethodCallExpression,
    SetExpression, ExportDeclaration, ImportDeclaration, ExportListDeclaration, TemplateStringExpression
)
from lexer import Lexer
from error_reporter import ErrorReporter, ErrorInfo, GerLangErrors
from call_stack import CallStack, CallFrame, RuntimeError as GerLangRuntimeError

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
            # Hier könnten wir später bessere Positionsinformationen hinzufügen
            raise GerLangRuntimeError(f"Variable '{name}' nicht definiert")

    def get(self, name):
        if name in self.vars:
            return self.vars[name]
        elif self.parent:
            return self.parent.get(name)
        else:
            # Hier könnten wir später bessere Positionsinformationen hinzufügen
            raise GerLangRuntimeError(f"Variable '{name}' nicht definiert")

class ReturnSignal(Exception):
    def __init__(self, value):
        self.value = value

class Interpreter:
    def __init__(self, current_file=None):
        self.globals = Environment()
        self.env = self.globals
        self.functions = {}
        self.current_file = current_file  # Aktueller Dateipfad für relative Imports
        self.error_reporter = ErrorReporter()
        self.call_stack = CallStack()

        # Builtins definieren
        self.setup_builtins()

    def setup_builtins(self):
        """Definiert alle eingebauten Funktionen"""
        # DRUCKE/ZEIGE für Output
        self.globals.define("DRUCKE", lambda *args: self._drucke_builtin(*args))
        self.globals.define("ZEIGE", lambda *args: self._drucke_builtin(*args))

        # LESE für Input
        self.globals.define("LESE", lambda prompt="": self._lese_builtin(prompt))

        # Type conversion functions
        self.globals.define("ZU_WORT", lambda value: self._zu_wort(value))
        self.globals.define("ZU_GANZ", lambda value: self._zu_ganz(value))
        self.globals.define("ZU_KOMMA", lambda value: self._zu_komma(value))
        
        # Math functions
        self.globals.define("WURZEL", lambda value: self._wurzel(value))
        self.globals.define("POTENZ", lambda base, exp: self._potenz(base, exp))
        self.globals.define("ABS", lambda value: self._abs(value))
        self.globals.define("RUNDEN", lambda value, digits=0: self._runden(value, digits))
        self.globals.define("ZUFALLSZAHL", lambda: self._zufallszahl())
        self.globals.define("ZUFALLSBEREICH", lambda min_val, max_val: self._zufallsbereich(min_val, max_val))

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
            haupt_func = self.functions["haupt"]
            if getattr(haupt_func, "return_type", None) not in ("GANZ", "int", "INT"):
                raise Exception("Die Funktion 'haupt' muss den Rückgabetyp GANZ (int) haben und einen Exit-Code zurückgeben!")
            return self.execute_function("haupt", [])

        return None

    def execute_function(self, name, args, call_site_node=None):
        """Führt eine Funktion aus"""
        func = self.functions.get(name)
        if not func:
            raise GerLangRuntimeError(
                f"Funktion '{name}' nicht gefunden",
                self.current_file or "",
                call_site_node.line if call_site_node else 1,
                call_site_node.column if call_site_node else 1,
                self.call_stack.get_stack_trace()
            )

        # Parameter-Anzahl prüfen
        if len(args) != len(func.parameters):
            raise GerLangRuntimeError(
                f"Funktion '{name}' erwartet {len(func.parameters)} Argumente, {len(args)} gegeben",
                self.current_file or "",
                call_site_node.line if call_site_node else 1,
                call_site_node.column if call_site_node else 1,
                self.call_stack.get_stack_trace()
            )

        # Call-Stack Frame hinzufügen
        self.call_stack.push(
            name, 
            self.current_file or "",
            call_site_node.line if call_site_node and hasattr(call_site_node, 'line') else 1,
            call_site_node.column if call_site_node and hasattr(call_site_node, 'column') else 1
        )

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
            result = None
        except ReturnSignal as r:
            result = r.value
        finally:
            # Call-Stack Frame entfernen
            self.call_stack.pop()
            # Umgebung zurücksetzen
            self.env = previous_env
        
        return result

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

        elif isinstance(stmt, TryCatchStatement):
            try:
                self.execute(stmt.try_block)
            except Exception as e:
                if stmt.catch_var:
                    # Fehler-Variable im neuen Scope setzen
                    # Verwende self.env als Parent, um Zugriff auf alle Variablen zu behalten
                    catch_env = Environment(self.env)
                    catch_env.define(stmt.catch_var, str(e))
                    previous_env = self.env
                    self.env = catch_env
                    try:
                        self.execute(stmt.catch_block)
                    finally:
                        self.env = previous_env
                else:
                    self.execute(stmt.catch_block)

        elif isinstance(stmt, SetExpression):
            # Ziel kann ArrayAccessExpression, PropertyAccessExpression oder IdentifierExpression sein
            value = self.evaluate(stmt.value)
            target = stmt.target
            if isinstance(target, ArrayAccessExpression):
                array = self.evaluate(target.array)
                index = self.evaluate(target.index)
                array[index] = value
            elif isinstance(target, PropertyAccessExpression):
                obj = self.evaluate(target.object_expr)
                prop = target.property_name
                setattr(obj, prop, value)  # (Optional: für spätere Objekte)
            elif isinstance(target, IdentifierExpression):
                self.env.assign(target.name, value)
            else:
                raise Exception(f"Zuweisung an diesen Ausdruck nicht unterstützt: {type(target)}")

        elif isinstance(stmt, ImportDeclaration):
            # Importiere Funktionen/Variablen aus externer Datei
            module_path = stmt.module
            if not os.path.isabs(module_path):
                # Relativ zur aktuellen Datei auflösen
                if self.current_file:
                    current_dir = os.path.dirname(self.current_file)
                    module_path = os.path.normpath(os.path.join(current_dir, module_path))
                else:
                    # Fallback: relativ zum aktuellen Arbeitsverzeichnis
                    module_path = os.path.normpath(os.path.join(os.getcwd(), module_path))
            if not os.path.exists(module_path):
                raise Exception(f"Import-Modul nicht gefunden: {stmt.module}")
            with open(module_path, encoding="utf-8") as f:
                code = f.read()
            tokens = Lexer(code).tokenize()
            from parser import Parser
            parser = Parser(tokens)
            mod_ast = parser.parse()
            # Sammle alle ExportDeclaration und ExportListDeclaration
            exports = {}
            # 1. Einzelne Exporte
            for s in mod_ast.statements:
                if isinstance(s, ExportDeclaration):
                    decl = s.declaration
                    if isinstance(decl, FunctionDeclaration):
                        exports[decl.name] = decl
                    elif isinstance(decl, VariableDeclaration):
                        exports[decl.name] = decl
            # 2. Export-Listen (GIBFREI name1, name2;)
            defined_names = {}
            for s in mod_ast.statements:
                if isinstance(s, FunctionDeclaration):
                    defined_names[s.name] = s
                elif isinstance(s, VariableDeclaration):
                    defined_names[s.name] = s
            for s in mod_ast.statements:
                if isinstance(s, ExportListDeclaration):
                    for name in s.names:
                        if name in defined_names:
                            exports[name] = defined_names[name]
                        else:
                            raise Exception(f"Exportierter Name '{name}' ist im Modul nicht definiert")
            # Importiere nur die gewünschten Namen
            for name in stmt.names:
                if name in exports:
                    decl = exports[name]
                    if isinstance(decl, FunctionDeclaration):
                        self.functions[name] = decl
                    elif isinstance(decl, VariableDeclaration):
                        value = self.evaluate(decl.initializer) if decl.initializer else None
                        self.env.define(name, value)
                    else:
                        raise Exception(f"Exportierter Name '{name}' ist kein unterstützter Typ")
                else:
                    raise Exception(f"'{name}' ist nicht als exportiert in {stmt.module} deklariert")
            return
        elif isinstance(stmt, ExportDeclaration):
            # Export-Statements werden zur Laufzeit ignoriert (Modul-Handling erfolgt beim Parsen/AST)
            return
        elif isinstance(stmt, ExportListDeclaration):
            # Export-Listen werden zur Laufzeit ignoriert (nur für Modul-Analyse)
            return
        else:
            raise Exception(f"Unbekanntes Statement: {type(stmt)}")

    def evaluate(self, expr):
        """Evaluiert einen Ausdruck"""
        if isinstance(expr, LiteralExpression):
            return expr.value

        elif isinstance(expr, ArrayLiteralExpression):
            return [self.evaluate(el) for el in expr.elements]

        elif isinstance(expr, TemplateStringExpression):
            return self.evaluate_template_string(expr)

        elif isinstance(expr, ArrayAccessExpression):
            array = self.evaluate(expr.array)
            index = self.evaluate(expr.index)
            return array[index]

        elif isinstance(expr, IdentifierExpression):
            try:
                return self.env.get(expr.name)
            except GerLangRuntimeError as e:
                # Füge Positionsinformationen hinzu
                raise GerLangRuntimeError(
                    e.message,
                    self.current_file or "",
                    expr.line,
                    expr.column,
                    self.call_stack.get_stack_trace()
                )

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
                    raise GerLangRuntimeError(
                        "Division durch Null",
                        self.current_file or "",
                        expr.line,
                        expr.column,
                        self.call_stack.get_stack_trace()
                    )
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

                # Erst in globalen Builtins suchen
                try:
                    func = self.globals.get(func_name)
                    if callable(func):
                        args = [self.evaluate(arg) for arg in expr.arguments]
                        return func(*args)
                except GerLangRuntimeError:
                    # Variable nicht gefunden - weitersuchen
                    pass
                except Exception as e:
                    # Ausführungsfehler in der Funktion - direkt weiterwerfen
                    raise e

                # Dann im aktuellen Environment suchen
                try:
                    func = self.env.get(func_name)
                    if callable(func):
                        args = [self.evaluate(arg) for arg in expr.arguments]
                        return func(*args)
                except GerLangRuntimeError:
                    # Variable nicht gefunden - weitersuchen
                    pass
                except Exception as e:
                    # Ausführungsfehler in der Funktion - direkt weiterwerfen
                    raise e

                # Dann in benutzerdefinierten Funktionen
                if func_name in self.functions:
                    args = [self.evaluate(arg) for arg in expr.arguments]
                    return self.execute_function(func_name, args, expr)

                raise GerLangRuntimeError(
                    f"Unbekannte Funktion: {func_name}",
                    self.current_file or "",
                    expr.line,
                    expr.column,
                    self.call_stack.get_stack_trace()
                )
            else:
                # Komplexerer Funktionsausdruck
                func = self.evaluate(expr.function)
                if callable(func):
                    args = [self.evaluate(arg) for arg in expr.arguments]
                    return func(*args)
                else:
                    raise Exception("Ausdruck ist nicht aufrufbar")

        elif isinstance(expr, PropertyAccessExpression):
            obj = self.evaluate(expr.object_expr)
            prop = expr.property_name
            # Property-Dispatch für eingebaute Typen
            if isinstance(obj, str) and prop == "LÄNGE":
                return len(obj)
            if isinstance(obj, list) and prop == "LÄNGE":
                return len(obj)
            raise Exception(f"Unbekannte Property '{prop}' für Typ {type(obj).__name__}")

        elif isinstance(expr, MethodCallExpression):
            obj = self.evaluate(expr.object_expr)
            method = expr.method_name
            args = [self.evaluate(arg) for arg in expr.arguments]
            # Methoden-Dispatch für eingebaute Typen
            if isinstance(obj, list):
                if method == "HINZUFÜGEN":
                    obj.insert(0, args[0])
                    return None
                if method == "ERWEITERN":
                    obj.append(args[0])
                    return None
                if method == "LÄNGE":
                    return len(obj)
            if isinstance(obj, str):
                if method == "LÄNGE":
                    return len(obj)
            raise Exception(f"Unbekannte Methode '{method}' für Typ {type(obj).__name__}")

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

    def _wurzel(self, value):
        """Berechnet die Quadratwurzel"""
        try:
            if value < 0:
                raise Exception("Wurzel aus negativer Zahl ist nicht erlaubt")
            return math.sqrt(float(value))
        except (ValueError, TypeError):
            raise Exception(f"Kann WURZEL von '{value}' nicht berechnen")

    def _potenz(self, base, exponent):
        """Berechnet base^exponent"""
        try:
            return math.pow(float(base), float(exponent))
        except (ValueError, TypeError):
            raise Exception(f"Kann POTENZ({base}, {exponent}) nicht berechnen")

    def _abs(self, value):
        """Berechnet den Absolutwert"""
        try:
            return abs(float(value))
        except (ValueError, TypeError):
            raise Exception(f"Kann ABS von '{value}' nicht berechnen")

    def _runden(self, value, digits=0):
        """Rundet eine Zahl auf die angegebene Anzahl Nachkommastellen"""
        try:
            if digits == 0:
                return round(float(value))
            return round(float(value), int(digits))
        except (ValueError, TypeError):
            raise Exception(f"Kann '{value}' nicht runden")

    def _zufallszahl(self):
        """Gibt eine Zufallszahl zwischen 0.0 und 1.0 zurück"""
        return random.random()

    def _zufallsbereich(self, min_val, max_val):
        """Gibt eine Zufallszahl im angegebenen Bereich zurück"""
        try:
            min_val = int(min_val)
            max_val = int(max_val)
            return random.randint(min_val, max_val)
        except (ValueError, TypeError):
            raise Exception(f"ZUFALLSBEREICH({min_val}, {max_val}) - ungültige Parameter")

    def evaluate_template_string(self, expr: TemplateStringExpression):
        """Evaluiert einen Template-String mit ${...} Interpolation"""
        result = ""
        
        # Template-Format: part0 + expr0 + part1 + expr1 + ... + partN
        for i in range(len(expr.expressions)):
            # String-Teil vor der Expression
            if i < len(expr.parts):
                result += expr.parts[i]
            
            # Evaluiere die Expression und konvertiere zu String
            expr_value = self.evaluate(expr.expressions[i])
            result += str(expr_value)
        
        # Letzten String-Teil anhängen (falls vorhanden)
        if len(expr.parts) > len(expr.expressions):
            result += expr.parts[-1]
        
        return result