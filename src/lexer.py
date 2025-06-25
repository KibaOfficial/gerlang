# Copyright (c) 2025 KibaOfficial
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT
import re
from typing import List, NamedTuple, Optional
from tokens import KEYWORDS, LITERALS, OPERATORS

# Ein-Zeichen Operatoren und Delimiters
single_char_tokens = {
  '(': 'LPAREN',
  ')': 'RPAREN', 
  '{': 'LBRACE',
  '}': 'RBRACE',
  '[': 'LBRACKET',
  ']': 'RBRACKET',
  ';': 'SEMICOLON',
  ',': 'COMMA',
  '.': 'DOT',
  '+': 'PLUS',
  '-': 'MINUS',
  '*': 'MULTIPLY',
  '/': 'DIVIDE',
  '%': 'MODULO',
  '=': 'ASSIGN',
  '<': 'LT',
  '>': 'GT',
  '!': 'NOT'
}

class Token(NamedTuple):
  type: str
  value: str
  line: int
  column: int

class Lexer:
  def __init__(self, source: str):
    self.source = source
    self.position = 0
    self.line = 1
    self.column = 1
    self.tokens = []

  def current_char(self) -> Optional[str]:
    if self.position >= len(self.source):
      return None
    return self.source[self.position]

  def peek_char(self, offset: int = 1) -> Optional[str]:
    peek_pos = self.position + offset
    if peek_pos >= len(self.source):
      return None
    return self.source[peek_pos]

  def advance(self):
    if (self.position < len(self.source) and self.source[self.position] == '\n'):
      self.line += 1
      self.column = 1
    else:
      self.column += 1
    self.position += 1

  def skip_whitespace(self):
    while self.current_char() is not None and self.current_char().isspace():
      self.advance()
  
  def skip_comment(self):
    # Einzeilige Kommentare mit // oder HINWEIS:
    if self.current_char() == '/' and self.peek_char() == '/':
        while self.current_char() and self.current_char() != '\n':
            self.advance()
    elif self.match_word("HINWEIS:"):
        # Überspringe "HINWEIS:" erst
        for _ in range(8):  # Länge von "HINWEIS:"
            self.advance()
        while self.current_char() and self.current_char() != '\n':
            self.advance()

  def match_word(self, word: str) -> bool:
    """Prüft ob das aktuelle Wort mit dem gegebenen Wort übereinstimmt"""
    if self.position + len(word) > len(self.source):
      return False
    return self.source[self.position:self.position + len(word)] == word
  
  def read_string(self) -> str:
    """Liest einen String zwischen Anführungszeichen"""
    quote_char = self.current_char() # " oder '
    self.advance()  # Anführungszeichen überspringen

    value = ""
    while self.current_char() and self.current_char() != quote_char:
      if self.current_char() == '\\': # Escape-Sequenz
        self.advance()
        if self.current_char() == 'n':
          value += '\n'
        elif self.current_char() == 't':
          value += '\t'
        elif self.current_char() == '\\':
            value += '\\'
        elif self.current_char() == quote_char:
          value += quote_char
        else:
          value += self.current_char()
      else:
        value += self.current_char()
      self.advance()
    if self.current_char() == quote_char:
      self.advance()
    else:
      raise SyntaxError(f"Unterminated string at line {self.line}, column {self.column}")
    return value

  def read_number(self) -> str:
    """Liest eine Zahl (int oder float)"""
    value = ""
    has_dot = False
    
    while self.current_char() and (self.current_char().isdigit() or self.current_char() == '.'):
      if self.current_char() == '.':
        if has_dot:
            break
        has_dot = True
      value += self.current_char()
      self.advance()

    
    return value
  
  def read_identifier(self) -> str:
    """Liest einen Identifier (Variablennamen, Keywords, etc.)"""
    value = ""

    while (self.current_char() and 
            (self.current_char().isalnum() or 
              self.current_char() in '_ÄÖÜäöüß')):
            value += self.current_char()
            self.advance()
    return value
  
  def tokenize(self) -> List[Token]:
    """Hauptfunktion - zerlegt den Quellcode in Tokens"""
    while self.current_char():
      self.skip_whitespace()

      if not self.current_char():
        break

      # Kommentare
      if (self.current_char() == '/' and self.peek_char() == '/') or self.match_word("HINWEIS:"):
        self.skip_comment()
        continue

      # Strings
      if self.current_char() in '"\'':
        line, col = self.line, self.column
        string_value = self.read_string()
        self.tokens.append(Token("STRING_LITERAL", string_value, line, col))
        continue
      
      # Zahlen
      if self.current_char().isdigit():
        line, col = self.line, self.column
        number = self.read_number()
        token_type = "FLOAT_LITERAL" if '.' in number else "INT_LITERAL"
        self.tokens.append(Token(token_type, number, line, col))
        continue

      # Zwei-Zeichen-Operatoren
      two_char = self.source[self.position:self.position + 2] if self.position + 1 < len(self.source) else ""
      if two_char in ["==", "!=", "<=", ">=", "&&", "||", "++"]:
        line, col = self.line, self.column
        self.advance()
        self.advance()
        self.tokens.append(Token(two_char, two_char, line, col))
        continue

      if self.current_char() in single_char_tokens:
        line, col = self.line, self.column
        char = self.current_char()
        self.advance()
        self.tokens.append(Token(single_char_tokens[char], char, line, col))
        continue
      
      # Identifiers und Keywords
      if self.current_char().isalpha() or self.current_char() in '_ÄÖÜäöüß':
        line, col = self.line, self.column
        identifier = self.read_identifier()
        
        # Prüfe ob es ein Keyword ist
        if identifier in KEYWORDS:
            self.tokens.append(Token(KEYWORDS[identifier], identifier, line, col))
        elif identifier in LITERALS:
            self.tokens.append(Token("BOOL_LITERAL", identifier, line, col))
        elif identifier in OPERATORS:
            mapped_op = OPERATORS[identifier]
            self.tokens.append(Token(mapped_op, identifier, line, col))
        else:
            self.tokens.append(Token("IDENTIFIER", identifier, line, col))
        continue

      # Unbekanntes Zeichen
      raise SyntaxError(f"Unexpected character '{self.current_char()}' at line {self.line}, column {self.column}")
    
    # EOF Token
    self.tokens.append(Token("EOF", "", self.line, self.column))
    return self.tokens