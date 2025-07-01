# Copyright (c) 2025 KibaOfficial
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

"""
Built-in Funktionen für GerLang 4.1.0
Alle eingebauten Funktionen sind hier zentralisiert
"""

import math
import random
import sys
from typing import Any, Union


class BuiltinFunctions:
    """Container für alle Built-in Funktionen von GerLang"""
    
    @staticmethod
    def setup_builtins(environment):
        """Registriert alle Built-in Funktionen in der globalen Umgebung"""
        
        # I/O Funktionen
        environment.define("DRUCKE", BuiltinFunctions._drucke_builtin)
        environment.define("ZEIGE", BuiltinFunctions._drucke_builtin)
        environment.define("LESE", BuiltinFunctions._lese_builtin)
        
        # Type conversion functions
        environment.define("ZU_WORT", BuiltinFunctions._zu_wort)
        environment.define("ZU_GANZ", BuiltinFunctions._zu_ganz)
        environment.define("ZU_KOMMA", BuiltinFunctions._zu_komma)
        
        # Math functions
        environment.define("WURZEL", BuiltinFunctions._wurzel)
        environment.define("POTENZ", BuiltinFunctions._potenz)
        environment.define("ABS", BuiltinFunctions._abs)
        environment.define("RUNDEN", BuiltinFunctions._runden)
        environment.define("ZUFALLSZAHL", BuiltinFunctions._zufallszahl)
        environment.define("ZUFALLSBEREICH", BuiltinFunctions._zufallsbereich)

    # I/O Funktionen
    @staticmethod
    def _drucke_builtin(*args):
        """DRUCKE/ZEIGE - gibt Werte auf der Konsole aus"""
        output_parts = []
        for arg in args:
            if isinstance(arg, str):
                output_parts.append(arg)
            elif isinstance(arg, bool):
                output_parts.append("JA" if arg else "NEIN")
            elif arg is None:
                output_parts.append("NIX")
            elif isinstance(arg, list):
                # Array-Darstellung
                elements = []
                for item in arg:
                    if isinstance(item, str):
                        elements.append(f'"{item}"')
                    elif isinstance(item, bool):
                        elements.append("JA" if item else "NEIN")
                    elif item is None:
                        elements.append("NIX")
                    else:
                        elements.append(str(item))
                output_parts.append(f"[{', '.join(elements)}]")
            else:
                output_parts.append(str(arg))
        
        output = " ".join(output_parts)
        print(output)
        return None

    @staticmethod
    def _lese_builtin(prompt=""):
        """LESE - liest Eingabe von der Konsole"""
        try:
            if prompt:
                return input(str(prompt))
            else:
                return input()
        except (EOFError, KeyboardInterrupt):
            return ""

    # Type Conversion Functions
    @staticmethod
    def _zu_wort(value):
        """ZU_WORT - konvertiert zu String"""
        if value is None:
            return "NIX"
        elif isinstance(value, bool):
            return "JA" if value else "NEIN"
        elif isinstance(value, list):
            # Array zu String
            elements = [BuiltinFunctions._zu_wort(item) for item in value]
            return f"[{', '.join(elements)}]"
        else:
            return str(value)

    @staticmethod
    def _zu_ganz(value):
        """ZU_GANZ - konvertiert zu Integer"""
        if isinstance(value, int):
            return value
        elif isinstance(value, float):
            return int(value)
        elif isinstance(value, str):
            try:
                # Versuche zuerst Float, dann zu Int
                return int(float(value))
            except ValueError:
                raise ValueError(f"'{value}' kann nicht zu GANZ konvertiert werden")
        elif isinstance(value, bool):
            return 1 if value else 0
        elif value is None:
            return 0
        else:
            raise ValueError(f"Typ {type(value).__name__} kann nicht zu GANZ konvertiert werden")

    @staticmethod
    def _zu_komma(value):
        """ZU_KOMMA - konvertiert zu Float"""
        if isinstance(value, float):
            return value
        elif isinstance(value, int):
            return float(value)
        elif isinstance(value, str):
            try:
                return float(value)
            except ValueError:
                raise ValueError(f"'{value}' kann nicht zu KOMMA konvertiert werden")
        elif isinstance(value, bool):
            return 1.0 if value else 0.0
        elif value is None:
            return 0.0
        else:
            raise ValueError(f"Typ {type(value).__name__} kann nicht zu KOMMA konvertiert werden")

    # Math Functions
    @staticmethod
    def _wurzel(value):
        """WURZEL - berechnet Quadratwurzel"""
        try:
            num_value = float(value)
            if num_value < 0:
                raise ValueError("Quadratwurzel aus negativer Zahl nicht möglich")
            return math.sqrt(num_value)
        except (TypeError, ValueError) as e:
            raise ValueError(f"WURZEL: {e}")

    @staticmethod
    def _potenz(base, exponent):
        """POTENZ - berechnet base^exponent"""
        try:
            base_num = float(base)
            exp_num = float(exponent)
            return math.pow(base_num, exp_num)
        except (TypeError, ValueError) as e:
            raise ValueError(f"POTENZ: {e}")

    @staticmethod
    def _abs(value):
        """ABS - berechnet Absolutwert"""
        try:
            return abs(float(value))
        except (TypeError, ValueError) as e:
            raise ValueError(f"ABS: {e}")

    @staticmethod
    def _runden(value, digits=0):
        """RUNDEN - rundet eine Zahl"""
        try:
            num_value = float(value)
            digits_int = int(digits)
            return round(num_value, digits_int)
        except (TypeError, ValueError) as e:
            raise ValueError(f"RUNDEN: {e}")

    @staticmethod
    def _zufallszahl():
        """ZUFALLSZAHL - gibt Zufallszahl zwischen 0.0 und 1.0 zurück"""
        return random.random()

    @staticmethod
    def _zufallsbereich(min_val, max_val):
        """ZUFALLSBEREICH - gibt Zufallszahl im Bereich zurück"""
        try:
            min_int = int(min_val)
            max_int = int(max_val)
            if min_int > max_int:
                raise ValueError("min_val darf nicht größer als max_val sein")
            return random.randint(min_int, max_int)
        except (TypeError, ValueError) as e:
            raise ValueError(f"ZUFALLSBEREICH: {e}")
