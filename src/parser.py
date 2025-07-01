# Copyright (c) 2025 KibaOfficial
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from abc import ABC
from typing import List, Optional, Any
from lexer import Token

# ===== AST NODE DEFINITIONS =====

class ASTNode(ABC):
    def __init__(self):
        self.line = 1
        self.column = 1
    
    def set_position(self, line: int, column: int):
        self.line = line
        self.column = column
        return self

class Expression(ASTNode):
    pass

class Statement(ASTNode):
    pass

class LiteralExpression(Expression):
    def __init__(self, value: Any, type_name: str):
        super().__init__()
        self.value = value
        self.type_name = type_name
    def __repr__(self):
        return f"Literal({self.value}, {self.type_name})"

class IdentifierExpression(Expression):
    def __init__(self, name: str):
        super().__init__()
        self.name = name
    def __repr__(self):
        return f"Identifier({self.name})"

class BinaryExpression(Expression):
    def __init__(self, left: Expression, operator: str, right: Expression):
        super().__init__()
        self.left = left
        self.operator = operator
        self.right = right
    def __repr__(self):
        return f"Binary({self.left} {self.operator} {self.right})"

class UnaryExpression(Expression):
    def __init__(self, operator: str, operand: Expression):
        super().__init__()
        self.operator = operator
        self.operand = operand
    def __repr__(self):
        return f"Unary({self.operator} {self.operand})"

class CallExpression(Expression):
    def __init__(self, function: Expression, arguments: List[Expression]):
        super().__init__()
        self.function = function
        self.arguments = arguments
    def __repr__(self):
        return f"Call({self.function}, {self.arguments})"

class PropertyAccessExpression(Expression):
    def __init__(self, object_expr: Expression, property_name: str):
        super().__init__()
        self.object_expr = object_expr
        self.property_name = property_name
    def __repr__(self):
        return f"PropertyAccess({self.object_expr}.{self.property_name})"

class MethodCallExpression(Expression):
    def __init__(self, object_expr: Expression, method_name: str, arguments: List[Expression]):
        super().__init__()
        self.object_expr = object_expr
        self.method_name = method_name
        self.arguments = arguments
    def __repr__(self):
        return f"MethodCall({self.object_expr}.{self.method_name}({self.arguments}))"

class BlockStatement(Statement):
    def __init__(self, statements: List[Statement]):
        self.statements = statements
    def __repr__(self):
        return f"Block({len(self.statements)} statements)"

class ExpressionStatement(Statement):
    def __init__(self, expression: Expression):
        self.expression = expression
    def __repr__(self):
        return f"ExprStmt({self.expression})"

class VariableDeclaration(Statement):
    def __init__(self, type_name: str, name: str, initializer: Optional[Expression] = None):
        self.type_name = type_name
        self.name = name
        self.initializer = initializer
    def __repr__(self):
        return f"VarDecl({self.type_name} {self.name} = {self.initializer})"

class IfStatement(Statement):
    def __init__(self, condition: Expression, then_branch: Statement, else_branch: Optional[Statement] = None):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch
    def __repr__(self):
        return f"If({self.condition}, {self.then_branch}, {self.else_branch})"

class WhileStatement(Statement):
    def __init__(self, condition: Expression, body: Statement):
        self.condition = condition
        self.body = body
    def __repr__(self):
        return f"While({self.condition}, {self.body})"

class ForStatement(Statement):
    def __init__(self, initializer: Optional[Statement], condition: Optional[Expression],
                 increment: Optional[Statement], body: Statement):
        self.initializer = initializer
        self.condition = condition
        self.increment = increment
        self.body = body
    def __repr__(self):
        return f"For({self.initializer}, {self.condition}, {self.increment}, {self.body})"

class ReturnStatement(Statement):
    def __init__(self, value: Optional[Expression] = None):
        self.value = value
    def __repr__(self):
        return f"Return({self.value})"

class AssignmentStatement(Statement):
    def __init__(self, name: str, value: Expression):
        self.name = name
        self.value = value
    def __repr__(self):
        return f"Assignment({self.name} = {self.value})"

class FunctionDeclaration(Statement):
    def __init__(self, return_type: str, name: str, parameters: List[tuple], body: Statement):
        self.return_type = return_type
        self.name = name
        self.parameters = parameters  # List of (type, name) tuples
        self.body = body
    def __repr__(self):
        return f"Function({self.return_type} {self.name}({self.parameters}))"

# NEW: Print statement for DRUCKE
class PrintStatement(Statement):
    def __init__(self, expression: Expression):
        self.expression = expression
    def __repr__(self):
        return f"Print({self.expression})"

class ArrayLiteralExpression(Expression):
    def __init__(self, elements: List[Expression]):
        super().__init__()
        self.elements = elements
    def __repr__(self):
        return f"ArrayLiteral({self.elements})"

class ArrayAccessExpression(Expression):
    def __init__(self, array: Expression, index: Expression):
        super().__init__()
        self.array = array
        self.index = index
    def __repr__(self):
        return f"ArrayAccess({self.array}[{self.index}])"

class Program(ASTNode):
    def __init__(self, statements: List[Statement]):
        self.statements = statements
    def __repr__(self):
        return f"Program({len(self.statements)} statements)"

# NEW: TryCatchStatement for error handling
class TryCatchStatement(Statement):
    def __init__(self, try_block, catch_var, catch_block):
        self.try_block = try_block  # BlockStatement
        self.catch_var = catch_var  # Optional[str]
        self.catch_block = catch_block  # BlockStatement
    def __repr__(self):
        return f"TryCatch(try={self.try_block}, catch_var={self.catch_var}, catch={self.catch_block})"

# NEW: SetExpression for assignments to arbitrary expressions (e.g. array elements)
class SetExpression(Statement):
    def __init__(self, target: Expression, value: Expression):
        self.target = target
        self.value = value
    def __repr__(self):
        return f"Set({self.target} = {self.value})"

# NEW: Export and Import declarations
class ExportDeclaration(Statement):
    def __init__(self, declaration: Statement):
        self.declaration = declaration
    def __repr__(self):
        return f"Export({self.declaration})"

class ImportDeclaration(Statement):
    def __init__(self, names: List[str], module: str):
        self.names = names  # Liste der importierten Namen
        self.module = module  # Dateiname als String
    def __repr__(self):
        return f"Import({self.names} von {self.module})"

# NEW: Export list declaration for multiple exports
class ExportListDeclaration(Statement):
    def __init__(self, names: list):
        self.names = names
    def __repr__(self):
        return f"ExportList({self.names})"

# NEW: TemplateStringExpression for string interpolation
class TemplateStringExpression(Expression):
    def __init__(self, parts: List, expressions: List[Expression]):
        super().__init__()
        self.parts = parts  # String-Teile zwischen den Variablen
        self.expressions = expressions  # Ausdrücke für ${...}
    def __repr__(self):
        return f"TemplateString(parts={self.parts}, expressions={self.expressions})"

# ===== PARSER =====

class ParseError(Exception):
    def __init__(self, message: str, token: Token = None):
        super().__init__(message)
        self.token = token

class Parser:
    def __init__(self, tokens: List[Token], file_path: str = ""):
        self.tokens = tokens
        self.current = 0
        self.file_path = file_path

    def is_at_end(self) -> bool:
        return self.peek().type == "EOF"

    def peek(self) -> Token:
        return self.tokens[self.current]

    def previous(self) -> Token:
        return self.tokens[self.current - 1]

    def advance(self) -> Token:
        if not self.is_at_end():
            self.current += 1
        return self.previous()

    def check(self, token_type: str) -> bool:
        if self.is_at_end():
            return False
        return self.peek().type == token_type

    def match(self, *token_types: str) -> bool:
        for token_type in token_types:
            if self.check(token_type):
                self.advance()
                return True
        return False

    def consume(self, token_type: str, message: str) -> Token:
        if self.check(token_type):
            return self.advance()
        current_token = self.peek()
        raise ParseError(f"{message} bei Zeile {current_token.line}, Spalte {current_token.column}. Erwartet: '{token_type}', gefunden: '{current_token.value}'", current_token)

    def set_position(self, node: ASTNode, token: Token = None) -> ASTNode:
        """Setzt Positionsinformationen für einen AST-Node"""
        if token is None:
            token = self.previous()
        node.set_position(token.line, token.column)
        return node

    def parse(self) -> Program:
        statements = []
        while not self.is_at_end():
            stmt = self.declaration()
            if stmt:
                statements.append(stmt)
        return Program(statements)

    def declaration(self) -> Optional[Statement]:
        # try/except entfernt, Fehler werden im Hauptprogramm behandelt
        if self.match("EXPORT", "GIBFREI"):
            return self.export_declaration()
        if self.match("IMPORT", "HOLE"):
            return self.import_declaration()
        if self.check("VOID") or self.check("INT") or self.check("FLOAT") or self.check("STRING") or self.check("BOOL") or self.check("ARRAY"):
            # Nach Typ kommt Identifier
            type_token = self.peek()
            next_token = self.peek_next()
            if next_token.type == "IDENTIFIER":
                third_token = self.tokens[self.current + 2] if self.current + 2 < len(self.tokens) else None
                if third_token and third_token.type == "LPAREN":
                    return self.function_declaration()
                else:
                    return self.variable_declaration()
        return self.statement()

    def export_declaration(self) -> ExportDeclaration:
        # EXPORT oder GIBFREI wurde bereits konsumiert
        # Variante 1: Funktions- oder Variablendeklaration
        if self.check("VOID") or self.check("INT") or self.check("FLOAT") or self.check("STRING") or self.check("BOOL") or self.check("ARRAY"):
            type_token = self.peek()
            next_token = self.peek_next()
            if next_token.type == "IDENTIFIER":
                third_token = self.tokens[self.current + 2] if self.current + 2 < len(self.tokens) else None
                if third_token and third_token.type == "LPAREN":
                    decl = self.function_declaration()
                else:
                    decl = self.variable_declaration()
                return ExportDeclaration(decl)
        # Variante 2: GIBFREI name1, name2, ...;
        if self.check("IDENTIFIER"):
            names = [self.consume("IDENTIFIER", "Expected name to export").value]
            while self.match("COMMA"):
                if self.check("IDENTIFIER"):
                    names.append(self.consume("IDENTIFIER", "Expected name to export").value)
                else:
                    raise ParseError("Expected name to export after ',' in export statement")
            if self.check("SEMICOLON"):
                self.advance()
            elif not self.is_at_end() and self.peek().type != "EOF":
                raise ParseError("Expected ';' after export statement")
            return ExportListDeclaration(names)
        raise ParseError("Expected function or variable declaration or name list after 'gibfrei'")

    def import_declaration(self) -> ImportDeclaration:
        # IMPORT oder HOLE wurde bereits konsumiert
        names = []
        # Akzeptiere beliebig viele IDENTIFIER, getrennt durch Kommas
        if self.check("IDENTIFIER"):
            names.append(self.consume("IDENTIFIER", "Expected name to import").value)
            while self.match("COMMA"):
                if self.check("IDENTIFIER"):
                    names.append(self.consume("IDENTIFIER", "Expected name to import").value)
                else:
                    raise ParseError("Expected name to import after ',' in import statement")
        else:
            raise ParseError("Expected name to import after 'hole'")
        self.consume("FROM", "Expected 'von' after import names")
        if self.check("STRING_LITERAL"):
            module = self.consume("STRING_LITERAL", "Expected module file name as string").value
        else:
            raise ParseError("Expected module file name as string after 'von'")
        # Akzeptiere optionales Semikolon oder Zeilenende
        if self.check("SEMICOLON"):
            self.advance()
        elif not self.is_at_end() and self.peek().type != "EOF":
            raise ParseError("Expected ';' after import statement")
        return ImportDeclaration(names, module)

    def function_declaration(self) -> FunctionDeclaration:
        return_type = self.advance().value  # NIX, GANZ, etc.
        name = self.consume("IDENTIFIER", "Expected function name").value
        self.consume("LPAREN", "Expected '(' after function name")
        parameters = []
        if not self.check("RPAREN"):
            while True:
                param_name = self.consume("IDENTIFIER", "Expected parameter name").value
                self.consume("COLON", "Expected ':' after parameter name")
                param_type = self.advance().value  # GANZ, KOMMA, etc.
                parameters.append((param_type, param_name))
                if not self.match("COMMA"):
                    break
        self.consume("RPAREN", "Expected ')' after parameters")
        self.consume("LBRACE", "Expected '{' before function body")
        body = self.block_statement()
        return FunctionDeclaration(return_type, name, parameters, body)

    def peek_next(self):
        if self.current + 1 < len(self.tokens):
            return self.tokens[self.current + 1]
        return self.tokens[-1]

    def assignment_statement(self):
        name = self.consume("IDENTIFIER", "Erwartete Variablennamen").value
        self.consume("ASSIGN", "Erwartete '=' bei Zuweisung").value
        value = self.expression()
        self.consume("SEMICOLON", "Erwartete ';' nach Zuweisung")
        return AssignmentStatement(name, value)

    def statement(self) -> Statement:
        if self.match("IF"):
            return self.if_statement()
        if self.match("WHILE"):
            return self.while_statement()
        if self.match("FOR"):
            return self.for_statement()
        if self.match("RETURN"):
            return self.return_statement()
        if self.match("LBRACE"):
            return self.block_statement()
        if self.match("PRINT"):
            return self.print_statement()
        if self.match("TRY"):  # VERSUCHE
            return self.try_catch_statement()
        if self.check("INT") or self.check("FLOAT") or self.check("STRING") or self.check("BOOL") or self.check("ARRAY"):
            return self.variable_declaration()
        # Assignment an beliebigen Ausdruck (z.B. Array-Element)
        expr = self.expression()
        if self.match("ASSIGN"):
            value = self.expression()
            self.consume("SEMICOLON", "Erwartete ';' nach Zuweisung")
            return SetExpression(expr, value)
        self.consume("SEMICOLON", "Erwartete ';' nach Ausdruck")
        return ExpressionStatement(expr)

    # NEW: Print statement parser
    def print_statement(self) -> PrintStatement:
        self.consume("LPAREN", "Expected '(' after 'DRUCKE'")
        expression = self.expression()
        self.consume("RPAREN", "Expected ')' after print expression")
        self.consume("SEMICOLON", "Expected ';' after print statement")
        return PrintStatement(expression)

    def if_statement(self) -> IfStatement:
        self.consume("LPAREN", "Expected '(' after 'WENN'")
        condition = self.expression()
        self.consume("RPAREN", "Expected ')' after if condition")
        then_branch = self.statement()
        else_branch = None
        if self.match("ELSE"):
            else_branch = self.statement()
        return IfStatement(condition, then_branch, else_branch)

    def while_statement(self) -> WhileStatement:
        self.consume("LPAREN", "Expected '(' after 'SOLANGE'")
        condition = self.expression()
        self.consume("RPAREN", "Expected ')' after while condition")
        body = self.statement()
        return WhileStatement(condition, body)

    def for_statement(self) -> ForStatement:
        self.consume("LPAREN", "Expected '(' after 'FÜR'")
        initializer = None
        if self.match("SEMICOLON"):
            initializer = None
        elif self.check("INT") or self.check("FLOAT") or self.check("STRING") or self.check("BOOL"):
            initializer = self.variable_declaration()
        elif self.check("IDENTIFIER") and self.peek_next().type == "ASSIGN":
            initializer = self.assignment_statement()
        else:
            initializer = self.expression_statement()
        condition = None
        if not self.check("SEMICOLON"):
            condition = self.expression()
        self.consume("SEMICOLON", "Expected ';' after for loop condition")
        increment = None
        if not self.check("RPAREN"):
            if self.check("IDENTIFIER") and self.peek_next().type == "ASSIGN":
                # Assignment als Inkrement
                name = self.consume("IDENTIFIER", "Expected variable name for assignment").value
                self.consume("ASSIGN", "Expected '=' in assignment")
                value = self.expression()
                increment = AssignmentStatement(name, value)
            else:
                expr = self.expression()
                increment = ExpressionStatement(expr)
        self.consume("RPAREN", "Expected ')' after for clauses")
        body = self.statement()
        return ForStatement(initializer, condition, increment, body)

    def return_statement(self) -> ReturnStatement:
        value = None
        if not self.check("SEMICOLON"):
            value = self.expression()
        self.consume("SEMICOLON", "Expected ';' after return value")
        return ReturnStatement(value)

    def variable_declaration(self) -> VariableDeclaration:
        type_name = self.advance().value
        name = self.consume("IDENTIFIER", "Expected variable name").value
        initializer = None
        if self.match("ASSIGN"):
            initializer = self.expression()
        self.consume("SEMICOLON", "Expected ';' after variable declaration")
        return VariableDeclaration(type_name, name, initializer)

    def block_statement(self) -> BlockStatement:
        statements = []
        while not self.check("RBRACE") and not self.is_at_end():
            stmt = self.declaration()
            if stmt:
                statements.append(stmt)
        self.consume("RBRACE", "Expected '}' after block")
        return BlockStatement(statements)

    def expression_statement(self) -> ExpressionStatement:
        expr = self.expression()
        self.consume("SEMICOLON", "Expected ';' after expression")
        return ExpressionStatement(expr)

    def expression(self) -> Expression:
        return self.oder_expression()

    def oder_expression(self) -> Expression:
        expr = self.und_expression()
        while self.match("||", "ODER"):
            operator_token = self.previous()
            operator = operator_token.value
            right = self.und_expression()
            expr = self.set_position(BinaryExpression(expr, operator, right), operator_token)
        return expr

    def und_expression(self) -> Expression:
        expr = self.equality()
        while self.match("&&", "UND"):
            operator_token = self.previous()
            operator = operator_token.value
            right = self.equality()
            expr = self.set_position(BinaryExpression(expr, operator, right), operator_token)
        return expr

    def equality(self) -> Expression:
        expr = self.comparison()
        while self.match("==", "!="):
            operator_token = self.previous()
            operator = operator_token.value
            right = self.comparison()
            expr = self.set_position(BinaryExpression(expr, operator, right), operator_token)
        return expr

    def comparison(self) -> Expression:
        expr = self.term()
        while self.match("GT", ">=", "LT", "<="):
            operator_token = self.previous()
            operator = operator_token.value
            right = self.term()
            expr = self.set_position(BinaryExpression(expr, operator, right), operator_token)
        return expr

    def term(self) -> Expression:
        expr = self.factor()
        while self.match("MINUS", "PLUS"):
            operator_token = self.previous()
            operator = operator_token.value
            right = self.factor()
            expr = self.set_position(BinaryExpression(expr, operator, right), operator_token)
        return expr

    def factor(self) -> Expression:
        expr = self.unary()
        while self.match("DIVIDE", "MULTIPLY", "MODULO"):
            operator_token = self.previous()
            operator = operator_token.value
            right = self.unary()
            expr = self.set_position(BinaryExpression(expr, operator, right), operator_token)
        return expr

    def unary(self) -> Expression:
        if self.match("NOT", "MINUS"):
            operator_token = self.previous()
            operator = operator_token.value
            right = self.unary()
            return self.set_position(UnaryExpression(operator, right), operator_token)
        return self.call()

    def call(self) -> Expression:
        expr = self.primary()
        while True:
            if self.match("DOT"):
                dot_token = self.previous()
                method_or_property = self.consume("IDENTIFIER", "Expected property or method name after '.'").value
                if self.match("LPAREN"):
                    # Methodenaufruf: obj.METHODE(...)
                    arguments = []
                    if not self.check("RPAREN"):
                        arguments.append(self.expression())
                        while self.match("COMMA"):
                            arguments.append(self.expression())
                    self.consume("RPAREN", "Expected ')' after arguments")
                    expr = self.set_position(MethodCallExpression(expr, method_or_property, arguments), dot_token)
                else:
                    # Property-Access: obj.METHODE
                    expr = self.set_position(PropertyAccessExpression(expr, method_or_property), dot_token)
            elif self.match("LPAREN"):
                paren_token = self.previous()
                call_expr = self.finish_call(expr)
                expr = self.set_position(call_expr, paren_token)
            elif self.match("LBRACKET"):  # Array-Zugriff
                bracket_token = self.previous()
                index = self.expression()
                self.consume("RBRACKET", "Expected ']' after array index")
                expr = self.set_position(ArrayAccessExpression(expr, index), bracket_token)
            else:
                break
        return expr

    def finish_call(self, callee: Expression) -> CallExpression:
        arguments = []
        if not self.check("RPAREN"):
            arguments.append(self.expression())
            while self.match("COMMA"):
                arguments.append(self.expression())
        self.consume("RPAREN", "Expected ')' after arguments")
        return CallExpression(callee, arguments)

    def primary(self) -> Expression:
        if self.match("LBRACKET"):  # Array-Literal
            token = self.previous()
            elements = []
            if not self.check("RBRACKET"):
                elements.append(self.expression())
                while self.match("COMMA"):
                    elements.append(self.expression())
            self.consume("RBRACKET", "Expected ']' after array literal")
            return self.set_position(ArrayLiteralExpression(elements), token)
        if self.match("TEMPLATE_STRING_LITERAL"):  # Template-String
            token = self.previous()
            return self.set_position(self.parse_template_string_literal(token.value), token)
        if self.match("BOOL_LITERAL"):
            token = self.previous()
            value = token.value
            if value == "JA":
                return self.set_position(LiteralExpression(True, "BOOL"), token)
            else:
                return self.set_position(LiteralExpression(False, "BOOL"), token)
        if self.match("STRING_LITERAL"):
            token = self.previous()
            return self.set_position(LiteralExpression(token.value, "STRING"), token)
        if self.match("INT_LITERAL"):
            token = self.previous()
            return self.set_position(LiteralExpression(int(token.value), "INT"), token)
        if self.match("FLOAT_LITERAL"):
            token = self.previous()
            return self.set_position(LiteralExpression(float(token.value), "FLOAT"), token)
        if self.match("IDENTIFIER"):
            token = self.previous()
            return self.set_position(IdentifierExpression(token.value), token)
        if self.match("LPAREN"):
            expr = self.expression()
            self.consume("RPAREN", "Expected ')' after expression")
            return expr
        
        # Unerwartetes Token mit Position information
        token = self.peek()
        raise ParseError(f"Unexpected token '{token.value}'", token)

    def synchronize(self):
        self.advance()
        while not self.is_at_end():
            if self.previous().type == "SEMICOLON":
                return
            if self.peek().type in ["IF", "FOR", "WHILE", "RETURN", "VOID", "INT", "FLOAT", "STRING", "BOOL", "PRINT"]:
                return
            self.advance()

    def try_catch_statement(self) -> TryCatchStatement:
        self.consume("LPAREN", "Expected '(' after 'VERSUCHE'")
        self.consume("RPAREN", "Expected ')' after 'VERSUCHE'")
        try_block = self.statement()
        catch_var = None
        catch_block = None
        if self.match("CATCH"):  # FANGE
            if self.check("IDENTIFIER"):
                catch_var = self.consume("IDENTIFIER", "Expected error variable after 'FANGE'").value
            self.consume("LBRACE", "Expected '{' after 'FANGE'")
            catch_block = self.block_statement()
        else:
            raise ParseError("Expected 'FANGE' after 'VERSUCHE'-Block")
        return TryCatchStatement(try_block, catch_var, catch_block)

    def parse_template_string_literal(self, template_string: str) -> TemplateStringExpression:
        """Parst einen Template-String-Literal in parts und expressions"""
        import re
        
        parts = []
        expressions = []
        
        # Finde alle ${...} Teile
        pattern = r'\$\{([^}]+)\}'
        last_end = 0
        
        for match in re.finditer(pattern, template_string):
            # String-Teil vor der Expression
            part_before = template_string[last_end:match.start()]
            parts.append(part_before)
            
            # Expression-Inhalt parsen
            expr_content = match.group(1)
            
            # Mini-Parser für die Expression
            from lexer import Lexer
            expr_lexer = Lexer(expr_content)
            expr_tokens = expr_lexer.tokenize()
            
            # Erstelle einen Mini-Parser für die Expression
            expr_parser = Parser(expr_tokens)
            expr = expr_parser.expression()
            expressions.append(expr)
            
            last_end = match.end()
        
        # Letzten String-Teil hinzufügen
        final_part = template_string[last_end:]
        parts.append(final_part)
        
        return TemplateStringExpression(parts, expressions)

if __name__ == "__main__":
    import sys
    from lexer import Lexer
    if len(sys.argv) > 1 and sys.argv[1] == "ast":
        # Beispiel: python parser.py ast examples/imports/main.gerl
        filename = sys.argv[2]
        with open(filename, encoding="utf-8") as f:
            code = f.read()
        tokens = Lexer(code).tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        print(ast)