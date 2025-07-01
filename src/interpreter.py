# Copyright (c) 2025 KibaOfficial
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

"""
GerLang Interpreter 4.1.0 - Modernisiert und modularisiert
Hauptklasse für die Interpretation von GerLang-Code
"""

import os
from parser import Program, FunctionDeclaration
from environment import Environment
from gerlang_builtins import BuiltinFunctions
from statement_executor import StatementExecutor, ReturnSignal
from expression_evaluator import ExpressionEvaluator
from error_reporter import ErrorReporter, ErrorInfo, GerLangErrors
from call_stack import CallStack, CallFrame, RuntimeError as GerLangRuntimeError


class Interpreter:
    """Hauptklasse für die Interpretation von GerLang-Code"""
    
    def __init__(self, current_file=None):
        """Initialisiert den Interpreter"""
        self.globals = Environment()
        self.env = self.globals
        self.functions = {}
        self.current_file = current_file  # Aktueller Dateipfad für relative Imports
        self.error_reporter = ErrorReporter()
        self.call_stack = CallStack()
        
        # Module für Statement- und Expression-Handling
        self.statement_executor = StatementExecutor(self)
        self.expression_evaluator = ExpressionEvaluator(self)
        
        # Built-in Funktionen registrieren
        BuiltinFunctions.setup_builtins(self.globals)

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
        """Führt ein Statement aus - delegiert an StatementExecutor"""
        return self.statement_executor.execute(stmt)

    def evaluate(self, expr):
        """Evaluiert eine Expression - delegiert an ExpressionEvaluator"""
        return self.expression_evaluator.evaluate(expr)

    def is_truthy(self, value):
        """Bestimmt ob ein Wert als 'wahr' interpretiert wird"""
        if value is None:
            return False
        elif isinstance(value, bool):
            return value
        elif isinstance(value, (int, float)):
            return value != 0
        elif isinstance(value, str):
            return len(value) > 0
        elif isinstance(value, list):
            return len(value) > 0
        else:
            return True
