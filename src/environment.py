# Copyright (c) 2025 KibaOfficial
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

"""
Environment-Management für GerLang 4.1.0
Verwaltet Variablen-Scopes und Umgebungen
"""

from call_stack import RuntimeError as GerLangRuntimeError


class Environment:
    """Umgebung für Variablen-Scopes"""
    
    def __init__(self, parent=None):
        self.vars = {}
        self.parent = parent

    def define(self, name, value):
        """Definiert eine neue Variable in diesem Scope"""
        self.vars[name] = value

    def assign(self, name, value):
        """Weist einer existierenden Variable einen neuen Wert zu"""
        if name in self.vars:
            self.vars[name] = value
        elif self.parent:
            self.parent.assign(name, value)
        else:
            raise GerLangRuntimeError(f"Variable '{name}' nicht definiert")

    def get(self, name):
        """Holt den Wert einer Variable"""
        if name in self.vars:
            return self.vars[name]
        elif self.parent:
            return self.parent.get(name)
        else:
            raise GerLangRuntimeError(f"Variable '{name}' nicht definiert")

    def has(self, name):
        """Prüft ob eine Variable existiert"""
        return name in self.vars or (self.parent and self.parent.has(name))

    def delete(self, name):
        """Löscht eine Variable aus diesem Scope"""
        if name in self.vars:
            del self.vars[name]
        elif self.parent:
            self.parent.delete(name)
        else:
            raise GerLangRuntimeError(f"Variable '{name}' nicht definiert")

    def get_all_vars(self):
        """Gibt alle Variablen dieses Scopes zurück (für Debugging)"""
        result = {}
        if self.parent:
            result.update(self.parent.get_all_vars())
        result.update(self.vars)
        return result
