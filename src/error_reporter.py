# Copyright (c) 2025 KibaOfficial
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import os
from typing import Optional, List
from dataclasses import dataclass

@dataclass
class ErrorInfo:
    """Informationen über einen Fehler"""
    code: str           # GL001, GL002, etc.
    title: str          # Kurze Beschreibung
    file_path: str      # Dateipfad
    line: int           # Zeilennummer (1-basiert)
    column: int         # Spaltennummer (1-basiert)
    length: int = 1     # Länge des fehlerhaften Bereichs
    message: str = ""   # Detaillierte Nachricht
    hint: str = ""      # Hilfreicher Tipp
    severity: str = "error"  # error, warning, info

class ErrorReporter:
    """TypeScript-Style Fehlerberichterstattung für GerLang"""
    
    def __init__(self, source_code: str = "", file_path: str = ""):
        self.source_code = source_code
        self.file_path = file_path
        self.source_lines = source_code.splitlines() if source_code else []
    
    def report_error(self, error: ErrorInfo) -> str:
        """Generiert eine TypeScript-Style Fehlermeldung"""
        
        # Farben für Terminal (ANSI codes)
        RED = '\033[91m'
        BLUE = '\033[94m'
        YELLOW = '\033[93m'
        GREEN = '\033[92m'
        BOLD = '\033[1m'
        RESET = '\033[0m'
        
        # Basis-Fehlermeldung
        severity_color = RED if error.severity == "error" else YELLOW
        result = f"{severity_color}{BOLD}Fehler {error.code}{RESET}: {error.title}\n"
        
        # Datei-Pfad und Position
        result += f"{BLUE}  --> {error.file_path}:{error.line}:{error.column}{RESET}\n"
        
        # Kontext-Anzeige
        if self.source_lines and 1 <= error.line <= len(self.source_lines):
            result += f"{BLUE}   |{RESET}\n"
            
            # Zeile(n) vor dem Fehler (falls vorhanden)
            if error.line > 1:
                prev_line = self.source_lines[error.line - 2]
                result += f"{BLUE} {error.line - 1:2} |{RESET} {prev_line}\n"
            
            # Die fehlerhafte Zeile
            error_line = self.source_lines[error.line - 1]
            result += f"{BLUE} {error.line:2} |{RESET} {error_line}\n"
            
            # Caret-Zeiger
            spaces = " " * (error.column - 1)
            carets = "^" * max(1, error.length)
            result += f"{BLUE}   |{RESET} {spaces}{RED}{carets}{RESET}\n"
            
            # Zeile(n) nach dem Fehler (falls vorhanden)
            if error.line < len(self.source_lines):
                next_line = self.source_lines[error.line]
                result += f"{BLUE} {error.line + 1:2} |{RESET} {next_line}\n"
            
            result += f"{BLUE}   |{RESET}\n"
        
        # Detaillierte Nachricht
        if error.message:
            result += f"   {error.message}\n"
        
        # Hilfreicher Tipp
        if error.hint:
            result += f"{GREEN}   = Tipp: {error.hint}{RESET}\n"
        
        return result
    
    def report_runtime_error(self, runtime_error) -> str:
        """Generiert eine Laufzeit-Fehlermeldung mit Stack-Trace"""
        
        # Farben für Terminal (ANSI codes)
        RED = '\033[91m'
        BLUE = '\033[94m'
        YELLOW = '\033[93m'
        GREEN = '\033[92m'
        BOLD = '\033[1m'
        RESET = '\033[0m'
        
        # Basis-Fehlermeldung
        result = f"{RED}{BOLD}Laufzeitfehler{RESET}: {runtime_error.message}\n"
        
        # Hauptfehler-Position
        result += f"{BLUE}  --> {runtime_error.file_path}:{runtime_error.line}:{runtime_error.column}{RESET}\n"
        
        # Kontext-Anzeige
        if self.source_lines and 1 <= runtime_error.line <= len(self.source_lines):
            result += f"{BLUE}   |{RESET}\n"
            
            # Zeile(n) vor dem Fehler (falls vorhanden)
            if runtime_error.line > 1:
                prev_line = self.source_lines[runtime_error.line - 2]
                result += f"{BLUE} {runtime_error.line - 1:2} |{RESET} {prev_line}\n"
            
            # Die fehlerhafte Zeile
            error_line = self.source_lines[runtime_error.line - 1]
            result += f"{BLUE} {runtime_error.line:2} |{RESET} {error_line}\n"
            
            # Caret-Zeiger
            spaces = " " * (runtime_error.column - 1)
            result += f"{BLUE}   |{RESET} {spaces}{RED}^{RESET}\n"
            
            result += f"{BLUE}   |{RESET}\n"
        
        # Stack-Trace anzeigen
        if runtime_error.call_stack:
            result += f"\n{BLUE}Call-Stack:{RESET}\n"
            for i, frame in enumerate(reversed(runtime_error.call_stack)):
                result += f"{BLUE}  {i+1}: {frame.function_name}(){RESET} in {frame.file_path}:{frame.line}:{frame.column}\n"
        
        return result
    
    def print_error(self, error: ErrorInfo):
        """Druckt eine Fehlermeldung auf die Konsole"""
        print(self.report_error(error))

# Vordefinierte Fehler-Codes und Meldungen
class GerLangErrors:
    """Sammlung aller GerLang Fehler-Codes"""
    
    @staticmethod
    def syntax_error(file_path: str, line: int, column: int, expected: str, found: str) -> ErrorInfo:
        return ErrorInfo(
            code="GL001",
            title=f"Syntax-Fehler: Erwartete '{expected}', gefunden '{found}'",
            file_path=file_path,
            line=line,
            column=column,
            message=f"Der Parser erwartete '{expected}', aber fand '{found}'",
            hint=f"Füge '{expected}' hinzu oder prüfe die Syntax"
        )
    
    @staticmethod
    def type_mismatch(file_path: str, line: int, column: int, expected: str, found: str) -> ErrorInfo:
        return ErrorInfo(
            code="GL002",
            title=f"Typ-Fehler: '{found}' kann nicht '{expected}' zugewiesen werden",
            file_path=file_path,
            line=line,
            column=column,
            message=f"Erwarteter Typ: {expected}, gefundener Typ: {found}",
            hint=f"Verwende eine Typ-Konvertierung oder ändere den Typ"
        )
    
    @staticmethod
    def undefined_variable(file_path: str, line: int, column: int, var_name: str) -> ErrorInfo:
        return ErrorInfo(
            code="GL003",
            title=f"Undefinierte Variable: '{var_name}'",
            file_path=file_path,
            line=line,
            column=column,
            message=f"Die Variable '{var_name}' wurde nicht deklariert",
            hint=f"Deklariere die Variable mit 'GANZ {var_name} = ...' oder ähnlich"
        )
    
    @staticmethod
    def undefined_function(file_path: str, line: int, column: int, func_name: str) -> ErrorInfo:
        return ErrorInfo(
            code="GL004",
            title=f"Undefinierte Funktion: '{func_name}'",
            file_path=file_path,
            line=line,
            column=column,
            message=f"Die Funktion '{func_name}' wurde nicht gefunden",
            hint=f"Definiere die Funktion oder prüfe die Schreibweise"
        )
    
    @staticmethod
    def wrong_argument_count(file_path: str, line: int, column: int, func_name: str, expected: int, found: int) -> ErrorInfo:
        return ErrorInfo(
            code="GL005",
            title=f"Falsche Argumentzahl für '{func_name}'",
            file_path=file_path,
            line=line,
            column=column,
            message=f"Funktion '{func_name}' erwartet {expected} Argumente, {found} gegeben",
            hint=f"Prüfe die Funktionsdefinition und passe die Argumentzahl an"
        )
    
    @staticmethod
    def division_by_zero(file_path: str, line: int, column: int) -> ErrorInfo:
        return ErrorInfo(
            code="GL006",
            title="Division durch Null",
            file_path=file_path,
            line=line,
            column=column,
            message="Division oder Modulo durch Null ist nicht erlaubt",
            hint="Prüfe den Divisor vor der Operation"
        )
    
    @staticmethod
    def import_not_found(file_path: str, line: int, column: int, module_name: str) -> ErrorInfo:
        return ErrorInfo(
            code="GL007",
            title=f"Modul nicht gefunden: '{module_name}'",
            file_path=file_path,
            line=line,
            column=column,
            message=f"Das Modul '{module_name}' konnte nicht gefunden werden",
            hint="Prüfe den Dateipfad und stelle sicher, dass die Datei existiert"
        )
    
    @staticmethod
    def export_not_found(file_path: str, line: int, column: int, name: str, module: str) -> ErrorInfo:
        return ErrorInfo(
            code="GL008",
            title=f"Export nicht gefunden: '{name}' in '{module}'",
            file_path=file_path,
            line=line,
            column=column,
            message=f"'{name}' ist nicht als exportiert in {module} deklariert",
            hint=f"Füge 'GIBFREI {name};' zum Modul hinzu oder prüfe die Schreibweise"
        )
