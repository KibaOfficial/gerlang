# Copyright (c) 2025 KibaOfficial
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

"""
Expression-Evaluator für GerLang 4.1.0
Evaluiert verschiedene Expression-Typen
"""

import re
from call_stack import RuntimeError as GerLangRuntimeError


class ExpressionEvaluator:
    """Evaluiert verschiedene Expression-Typen"""
    
    def __init__(self, interpreter):
        self.interpreter = interpreter
    
    def evaluate(self, expr):
        """Evaluiert eine Expression - Dispatcher-Methode"""
        from parser import (
            LiteralExpression, IdentifierExpression, BinaryExpression, UnaryExpression,
            CallExpression, ArrayLiteralExpression, ArrayAccessExpression,
            PropertyAccessExpression, MethodCallExpression, SetExpression,
            TemplateStringExpression
        )
        
        if isinstance(expr, LiteralExpression):
            return self._evaluate_literal(expr)
        elif isinstance(expr, IdentifierExpression):
            return self._evaluate_identifier(expr)
        elif isinstance(expr, BinaryExpression):
            return self._evaluate_binary(expr)
        elif isinstance(expr, UnaryExpression):
            return self._evaluate_unary(expr)
        elif isinstance(expr, CallExpression):
            return self._evaluate_call(expr)
        elif isinstance(expr, ArrayLiteralExpression):
            return self._evaluate_array_literal(expr)
        elif isinstance(expr, ArrayAccessExpression):
            return self._evaluate_array_access(expr)
        elif isinstance(expr, PropertyAccessExpression):
            return self._evaluate_property_access(expr)
        elif isinstance(expr, MethodCallExpression):
            return self._evaluate_method_call(expr)
        elif isinstance(expr, SetExpression):
            return self._evaluate_set(expr)
        elif isinstance(expr, TemplateStringExpression):
            return self._evaluate_template_string(expr)
        else:
            raise GerLangRuntimeError(f"Unbekannter Expression-Typ: {type(expr).__name__}")

    def _evaluate_literal(self, expr):
        """Evaluiert ein Literal"""
        return expr.value

    def _evaluate_identifier(self, expr):
        """Evaluiert einen Identifier"""
        return self.interpreter.env.get(expr.name)

    def _evaluate_binary(self, expr):
        """Evaluiert eine binäre Expression"""
        left = self.evaluate(expr.left)
        
        # Short-circuit evaluation für logische Operatoren
        if expr.operator == "UND":
            if not self.interpreter.is_truthy(left):
                return False
            right = self.evaluate(expr.right)
            return self.interpreter.is_truthy(right)
        elif expr.operator == "ODER":
            if self.interpreter.is_truthy(left):
                return True
            right = self.evaluate(expr.right)
            return self.interpreter.is_truthy(right)
        
        # Für alle anderen Operatoren beide Seiten evaluieren
        right = self.evaluate(expr.right)
        
        # Arithmetische Operatoren
        if expr.operator == "+":
            return left + right
        elif expr.operator == "-":
            return left - right
        elif expr.operator == "*":
            return left * right
        elif expr.operator == "/":
            if right == 0:
                raise GerLangRuntimeError("Division durch Null")
            return left / right
        elif expr.operator == "%":
            return left % right
        
        # Vergleichsoperatoren
        elif expr.operator == "==":
            return left == right
        elif expr.operator == "!=":
            return left != right
        elif expr.operator == "<":
            return left < right
        elif expr.operator == "<=":
            return left <= right
        elif expr.operator == ">":
            return left > right
        elif expr.operator == ">=":
            return left >= right
        elif expr.operator == "IST":
            return left == right
        
        else:
            raise GerLangRuntimeError(f"Unbekannter binärer Operator: {expr.operator}")

    def _evaluate_unary(self, expr):
        """Evaluiert eine unäre Expression"""
        operand = self.evaluate(expr.operand)
        
        if expr.operator == "-":
            return -operand
        elif expr.operator == "NICHT":
            return not self.interpreter.is_truthy(operand)
        else:
            raise GerLangRuntimeError(f"Unbekannter unärer Operator: {expr.operator}")

    def _evaluate_call(self, expr):
        """Evaluiert einen Funktionsaufruf"""
        # Argumente evaluieren
        args = [self.evaluate(arg) for arg in expr.arguments]
        
        # Funktionsname aus der Expression extrahieren
        if hasattr(expr.function, 'name'):
            func_name = expr.function.name
        else:
            # Für komplexere Ausdrücke müssten wir das evaluieren
            raise GerLangRuntimeError("Komplexe Funktionsausdrücke noch nicht unterstützt")
        
        # Prüfen ob es eine Built-in Funktion ist
        if self.interpreter.env.has(func_name):
            func = self.interpreter.env.get(func_name)
            if callable(func):
                try:
                    return func(*args)
                except Exception as e:
                    raise GerLangRuntimeError(f"Fehler in Built-in Funktion '{func_name}': {e}")
        
        # Benutzerdefinierte Funktion
        return self.interpreter.execute_function(func_name, args, expr)

    def _evaluate_array_literal(self, expr):
        """Evaluiert ein Array-Literal"""
        return [self.evaluate(elem) for elem in expr.elements]

    def _evaluate_array_access(self, expr):
        """Evaluiert Array-Zugriff"""
        array = self.evaluate(expr.array)
        index = self.evaluate(expr.index)
        
        if not isinstance(array, list):
            raise GerLangRuntimeError("Array-Zugriff nur auf KISTE möglich")
        
        try:
            index_int = int(index)
            if index_int < 0 or index_int >= len(array):
                raise GerLangRuntimeError(f"Array-Index {index_int} außerhalb der Grenzen")
            return array[index_int]
        except (TypeError, ValueError):
            raise GerLangRuntimeError("Array-Index muss eine Zahl sein")

    def _evaluate_property_access(self, expr):
        """Evaluiert Property-Zugriff (z.B. array.LÄNGE)"""
        obj = self.evaluate(expr.object_expr)
        
        if expr.property_name == "LÄNGE":
            if isinstance(obj, (list, str)):
                return len(obj)
            else:
                raise GerLangRuntimeError("LÄNGE nur für KISTE oder WORT verfügbar")
        else:
            raise GerLangRuntimeError(f"Unbekannte Property: {expr.property_name}")

    def _evaluate_method_call(self, expr):
        """Evaluiert Methoden-Aufruf (z.B. array.HINZUFÜGEN())"""
        obj = self.evaluate(expr.object_expr)
        args = [self.evaluate(arg) for arg in expr.arguments]
        
        if isinstance(obj, list):
            if expr.method_name == "HINZUFÜGEN":
                for arg in args:
                    obj.insert(0, arg)  # Am Anfang einfügen
                return None
            elif expr.method_name == "ERWEITERN":
                for arg in args:
                    obj.append(arg)  # Am Ende anhängen
                return None
            else:
                raise GerLangRuntimeError(f"Unbekannte Methode für KISTE: {expr.method_name}")
        else:
            raise GerLangRuntimeError(f"Methoden-Aufruf nur für KISTE möglich")

    def _evaluate_set(self, expr):
        """Evaluiert Set-Expression (Array-Element setzen)"""
        array = self.evaluate(expr.object)
        index = self.evaluate(expr.index)
        value = self.evaluate(expr.value)
        
        if not isinstance(array, list):
            raise GerLangRuntimeError("Set-Operation nur auf KISTE möglich")
        
        try:
            index_int = int(index)
            if index_int < 0 or index_int >= len(array):
                raise GerLangRuntimeError(f"Array-Index {index_int} außerhalb der Grenzen")
            array[index_int] = value
            return value
        except (TypeError, ValueError):
            raise GerLangRuntimeError("Array-Index muss eine Zahl sein")

    def _evaluate_template_string(self, expr):
        """Evaluiert Template-String mit Interpolation"""
        result = ""
        
        # Verarbeite parts und expressions abwechselnd
        for i, part in enumerate(expr.parts):
            # Füge String-Teil hinzu
            result += part
            
            # Füge evaluierte Expression hinzu (falls vorhanden)
            if i < len(expr.expressions):
                value = self.evaluate(expr.expressions[i])
                if isinstance(value, bool):
                    result += "JA" if value else "NEIN"
                elif value is None:
                    result += "NIX"
                elif isinstance(value, list):
                    # Array zu String
                    elements = []
                    for item in value:
                        if isinstance(item, str):
                            elements.append(f'"{item}"')
                        elif isinstance(item, bool):
                            elements.append("JA" if item else "NEIN")
                        elif item is None:
                            elements.append("NIX")
                        else:
                            elements.append(str(item))
                    result += f"[{', '.join(elements)}]"
                else:
                    result += str(value)
        
        return result
