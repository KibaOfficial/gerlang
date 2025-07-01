# Copyright (c) 2025 KibaOfficial
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from dataclasses import dataclass
from typing import List, Optional

@dataclass
class CallFrame:
    """Repräsentiert einen Funktionsaufruf im Call-Stack"""
    function_name: str
    file_path: str
    line: int
    column: int

@dataclass 
class RuntimeError(Exception):
    """Erweiterte Runtime-Fehler mit Positionsinformationen"""
    message: str
    file_path: str = ""
    line: int = 1
    column: int = 1
    call_stack: List[CallFrame] = None
    
    def __init__(self, message: str, file_path: str = "", line: int = 1, column: int = 1, call_stack: List[CallFrame] = None):
        super().__init__(message)
        self.message = message
        self.file_path = file_path
        self.line = line 
        self.column = column
        self.call_stack = call_stack or []

class CallStack:
    """Verwaltet den Call-Stack für bessere Fehlermeldungen"""
    
    def __init__(self):
        self.frames: List[CallFrame] = []
    
    def push(self, function_name: str, file_path: str, line: int, column: int):
        """Fügt einen neuen Frame zum Call-Stack hinzu"""
        frame = CallFrame(function_name, file_path, line, column)
        self.frames.append(frame)
    
    def pop(self):
        """Entfernt den obersten Frame vom Call-Stack"""
        if self.frames:
            self.frames.pop()
    
    def current_frame(self) -> Optional[CallFrame]:
        """Gibt den aktuellen Frame zurück"""
        return self.frames[-1] if self.frames else None
    
    def get_stack_trace(self) -> List[CallFrame]:
        """Gibt den kompletten Call-Stack zurück"""
        return self.frames.copy()
    
    def clear(self):
        """Leert den Call-Stack"""
        self.frames.clear()
