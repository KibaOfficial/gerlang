# Copyright (c) 2025 KibaOfficial
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

"""
Statement-Executor für GerLang 4.1.0
Führt verschiedene Statement-Typen aus
"""

from environment import Environment
from call_stack import RuntimeError as GerLangRuntimeError


class ReturnSignal(Exception):
    """Signal für Return-Statements"""
    def __init__(self, value):
        self.value = value


class StatementExecutor:
    """Führt verschiedene Statement-Typen aus"""
    
    def __init__(self, interpreter):
        self.interpreter = interpreter
    
    def execute(self, stmt):
        """Führt ein Statement aus - Dispatcher-Methode"""
        from parser import (
            BlockStatement, ExpressionStatement, VariableDeclaration, AssignmentStatement,
            IfStatement, WhileStatement, ForStatement, ReturnStatement, PrintStatement,
            TryCatchStatement, ExportDeclaration, ImportDeclaration, ExportListDeclaration
        )
        
        if isinstance(stmt, BlockStatement):
            return self._execute_block(stmt)
        elif isinstance(stmt, ExpressionStatement):
            return self._execute_expression(stmt)
        elif isinstance(stmt, VariableDeclaration):
            return self._execute_variable_declaration(stmt)
        elif isinstance(stmt, AssignmentStatement):
            return self._execute_assignment(stmt)
        elif isinstance(stmt, IfStatement):
            return self._execute_if(stmt)
        elif isinstance(stmt, WhileStatement):
            return self._execute_while(stmt)
        elif isinstance(stmt, ForStatement):
            return self._execute_for(stmt)
        elif isinstance(stmt, ReturnStatement):
            return self._execute_return(stmt)
        elif isinstance(stmt, PrintStatement):
            return self._execute_print(stmt)
        elif isinstance(stmt, TryCatchStatement):
            return self._execute_try_catch(stmt)
        elif isinstance(stmt, ExportDeclaration):
            return self._execute_export(stmt)
        elif isinstance(stmt, ImportDeclaration):
            return self._execute_import(stmt)
        elif isinstance(stmt, ExportListDeclaration):
            return self._execute_export_list(stmt)
        else:
            raise GerLangRuntimeError(f"Unbekannter Statement-Typ: {type(stmt).__name__}")

    def _execute_block(self, stmt):
        """Führt einen Block von Statements aus"""
        # Neue Scope für Block erstellen
        block_env = Environment(self.interpreter.env)
        previous_env = self.interpreter.env
        self.interpreter.env = block_env

        try:
            for s in stmt.statements:
                self.execute(s)
        finally:
            self.interpreter.env = previous_env

    def _execute_expression(self, stmt):
        """Führt ein Expression Statement aus"""
        self.interpreter.evaluate(stmt.expression)

    def _execute_variable_declaration(self, stmt):
        """Führt eine Variablen-Deklaration aus"""
        value = self.interpreter.evaluate(stmt.initializer) if stmt.initializer else None
        self.interpreter.env.define(stmt.name, value)

    def _execute_assignment(self, stmt):
        """Führt eine Zuweisung aus"""
        value = self.interpreter.evaluate(stmt.value)
        self.interpreter.env.assign(stmt.name, value)

    def _execute_if(self, stmt):
        """Führt eine If-Anweisung aus"""
        cond = self.interpreter.evaluate(stmt.condition)
        if self.interpreter.is_truthy(cond):
            self.execute(stmt.then_branch)
        elif stmt.else_branch:
            self.execute(stmt.else_branch)

    def _execute_while(self, stmt):
        """Führt eine While-Schleife aus"""
        while self.interpreter.is_truthy(self.interpreter.evaluate(stmt.condition)):
            self.execute(stmt.body)

    def _execute_for(self, stmt):
        """Führt eine For-Schleife aus"""
        # For-Loop Scope
        for_env = Environment(self.interpreter.env)
        previous_env = self.interpreter.env
        self.interpreter.env = for_env

        try:
            # Initializer
            if stmt.initializer:
                self.execute(stmt.initializer)

            # Loop
            while True:
                # Condition check
                if stmt.condition and not self.interpreter.is_truthy(self.interpreter.evaluate(stmt.condition)):
                    break

                # Body ausführen
                self.execute(stmt.body)

                # Increment
                if stmt.increment:
                    from parser import AssignmentStatement, ExpressionStatement
                    if isinstance(stmt.increment, (AssignmentStatement, ExpressionStatement)):
                        self.execute(stmt.increment)
                    else:
                        self.interpreter.evaluate(stmt.increment)
        finally:
            self.interpreter.env = previous_env

    def _execute_return(self, stmt):
        """Führt ein Return-Statement aus"""
        value = self.interpreter.evaluate(stmt.value) if stmt.value else None
        raise ReturnSignal(value)

    def _execute_print(self, stmt):
        """Führt ein Print-Statement aus"""
        value = self.interpreter.evaluate(stmt.expression)
        print(value)

    def _execute_try_catch(self, stmt):
        """Führt ein Try-Catch-Statement aus"""
        try:
            self.execute(stmt.try_block)
        except Exception as e:
            if stmt.catch_var:
                # Fehler-Variable im neuen Scope setzen
                catch_env = Environment(self.interpreter.env)
                catch_env.define(stmt.catch_var, str(e))
                previous_env = self.interpreter.env
                self.interpreter.env = catch_env
                try:
                    self.execute(stmt.catch_block)
                finally:
                    self.interpreter.env = previous_env
            else:
                self.execute(stmt.catch_block)

    def _execute_export(self, stmt):
        """Führt eine Export-Deklaration aus"""
        # Export-Funktionalität würde hier implementiert werden
        # Für jetzt nur als Platzhalter
        pass

    def _execute_import(self, stmt):
        """Führt eine Import-Deklaration aus"""
        # Import-Funktionalität würde hier implementiert werden
        # Für jetzt nur als Platzhalter
        pass

    def _execute_export_list(self, stmt):
        """Führt eine Export-List-Deklaration aus"""
        # Export-List-Funktionalität würde hier implementiert werden
        # Für jetzt nur als Platzhalter
        pass
