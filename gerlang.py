# Copyright (c) 2025 KibaOfficial
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import argparse
import sys
import os
from pathlib import Path

# Füge src-Verzeichnis zum Python-Pfad hinzu
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from lexer import Lexer, Token
from parser import Parser
from interpreter import Interpreter

def safe_print(text):
    """Sicherer Print der Unicode-Encoding-Probleme vermeidet"""
    try:
        print(text)
    except UnicodeEncodeError:
        # Fallback: Emojis entfernen
        import re
        # Entferne alle Unicode-Emojis
        emoji_pattern = re.compile("["
                                 u"\U0001F600-\U0001F64F"  # emoticons
                                 u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                 u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                 u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                 u"\U00002702-\U000027B0"
                                 u"\U000024C2-\U0001F251"
                                 "]+", flags=re.UNICODE)
        clean_text = emoji_pattern.sub('', text)
        print(clean_text)

def print_banner():
    """Zeigt das GerLang Banner"""
    safe_print("GerLang - Die deutsche Programmiersprache")
    safe_print("=" * 50)

def lexer_command(file_path: str, verbose: bool = False):
    """Führt nur den Lexer aus und zeigt die Tokens"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            source_code = f.read()

        if verbose:
            safe_print(f"📄 Datei: {file_path}")
            safe_print("📝 Quellcode:")
            safe_print("-" * 30)
            safe_print(source_code)
            safe_print("-" * 30)

        lexer = Lexer(source_code)
        tokens = lexer.tokenize()

        safe_print("\n🔍 Lexer-Analyse:")
        safe_print("-" * 50)

        for token in tokens:
            if token.type == "EOF":
                safe_print(f"{'EOF':<15} | {'<end>':<20} | Line {token.line:>2}, Col {token.column:>2}")
            else:
                # Kürze lange Values für bessere Darstellung
                display_value = token.value[:20] + "..." if len(token.value) > 20 else token.value
                safe_print(f"{token.type:<15} | {display_value:<20} | Line {token.line:>2}, Col {token.column:>2}")

        safe_print(f"\n✅ Lexer erfolgreich! {len(tokens)} Tokens erkannt.")

    except FileNotFoundError:
        safe_print(f"❌ Fehler: Datei '{file_path}' nicht gefunden!")
        sys.exit(1)
    except Exception as e:
        safe_print(f"❌ Lexer-Fehler: {e}")
        sys.exit(1)

def run_command(file_path: str):
    """Führt eine GerLang-Datei aus (jetzt mit Parser & Interpreter!)"""
    safe_print(f"🚀 Führe {file_path} aus...")

    def get_humorous_tip(msg):
        msg_lower = msg.lower()
        if "unexpected token" in msg_lower:
            return "Hinweis: Unerwartetes Token. Prüfe die Syntax an dieser Stelle."
        if "expected ';'" in msg_lower or "expected '}'" in msg_lower or "block" in msg_lower:
            return "Hinweis: Es fehlt vermutlich ein Semikolon oder eine schließende Klammer."
        if "type" in msg_lower or "typ" in msg_lower:
            return "Hinweis: Typfehler. Prüfe, ob die Typen der Variablen und Ausdrücke zusammenpassen."
        if "function" in msg_lower or "funktionsaufruf" in msg_lower:
            return "Hinweis: Funktionsaufruf oder -definition prüfen. Stimmen Name, Argumente und Klammern?"
        if "assign" in msg_lower or "zuweisung" in msg_lower:
            return "Hinweis: Zuweisung prüfen. Ist das '=' korrekt gesetzt?"
        return "Hinweis: Prüfe die Syntax und den Kontext der Fehlermeldung."

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            source_code = f.read()
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()
        parser = Parser(tokens, file_path=file_path)
        try:
            program = parser.parse()
        except Exception as e:
            # Importiere Error Reporter
            from src.error_reporter import ErrorReporter, GerLangErrors
            
            reporter = ErrorReporter(source_code, file_path)
            token = getattr(e, 'token', None)
            
            if token:
                # Parser-Fehler mit Token-Information
                error = GerLangErrors.syntax_error(
                    file_path=file_path,
                    line=token.line,
                    column=token.column,
                    expected="gültiges Token",
                    found=token.value
                )
                reporter.print_error(error)
            else:
                # Fallback für andere Fehler
                safe_print(f"\n❌ Parser-Fehler: {str(e)}")
                safe_print("Tipp: Prüfe die Syntax und den Kontext der Fehlermeldung.")
            sys.exit(2)
        interpreter = Interpreter(current_file=os.path.abspath(file_path))
        try:
            interpreter.interpret(program)
        except Exception as e:
            # Verbesserte Laufzeit-Fehlerbehandlung
            from error_reporter import ErrorReporter as ErrReporter, GerLangErrors
            from call_stack import RuntimeError as GerLangRuntimeError
            
            reporter = ErrReporter(source_code, file_path)
            
            # Prüfe ob es sich um einen GerLang Runtime-Error handelt
            if isinstance(e, GerLangRuntimeError):
                # Prüfe spezifische Fehlertypen für bessere Codes
                if "Division durch Null" in e.message:
                    error = GerLangErrors.division_by_zero(
                        file_path=e.file_path,
                        line=e.line,
                        column=e.column
                    )
                elif "nicht definiert" in e.message and "Variable" in e.message:
                    import re
                    match = re.search(r"Variable '([^']+)' nicht definiert", e.message)
                    var_name = match.group(1) if match else "unbekannt"
                    error = GerLangErrors.undefined_variable(
                        file_path=e.file_path,
                        line=e.line,
                        column=e.column,
                        var_name=var_name
                    )
                elif "nicht gefunden" in e.message and "Funktion" in e.message:
                    import re
                    match = re.search(r"Funktion '([^']+)' nicht gefunden", e.message)
                    func_name = match.group(1) if match else "unbekannt"
                    error = GerLangErrors.undefined_function(
                        file_path=e.file_path,
                        line=e.line,
                        column=e.column,
                        func_name=func_name
                    )
                else:
                    # Generischer Runtime-Error
                    error = ErrorInfo(
                        code="GL999",
                        title=e.message,
                        file_path=e.file_path,
                        line=e.line,
                        column=e.column,
                        message=e.message
                    )
                
                # Füge Stack-Trace hinzu falls vorhanden
                if e.call_stack:
                    stack_trace = "\n\nCall-Stack:"
                    for i, frame in enumerate(reversed(e.call_stack)):
                        stack_trace += f"\n  {i}: {frame.function_name}() at {frame.file_path}:{frame.line}:{frame.column}"
                    error.hint = stack_trace
                
                reporter.print_error(error)
            else:
                # Fallback für andere Laufzeit-Fehler
                msg = str(e)
                if "nicht definiert" in msg and "Variable" in msg:
                    # Extrahiere Variablennamen
                    import re
                    match = re.search(r"Variable '([^']+)' nicht definiert", msg)
                    var_name = match.group(1) if match else "unbekannt"
                    
                    error = GerLangErrors.undefined_variable(
                        file_path=file_path,
                        line=1,  # TODO: Bessere Positionserkennung
                        column=1,
                        var_name=var_name
                    )
                    reporter.print_error(error)
                elif "nicht gefunden" in msg and "Funktion" in msg:
                    # Funktions-Fehler
                    match = re.search(r"Funktion '([^']+)' nicht gefunden", msg)
                    func_name = match.group(1) if match else "unbekannt"
                    
                    error = GerLangErrors.undefined_function(
                        file_path=file_path,
                        line=1,  # TODO: Bessere Positionserkennung
                        column=1,
                        func_name=func_name
                    )
                    reporter.print_error(error)
                elif "Division durch Null" in msg:
                    error = GerLangErrors.division_by_zero(
                        file_path=file_path,
                        line=1,  # TODO: Bessere Positionserkennung
                        column=1
                    )
                    reporter.print_error(error)
                else:
                    # Fallback für andere Laufzeit-Fehler
                    safe_print(f"\n❌ Laufzeitfehler: {msg}")
                    safe_print("Tipp: Vielleicht hast du eine Variable vergessen, einen Typen verwechselt oder die Wurst zu früh gegessen.")
            sys.exit(3)
        safe_print("\n✅ Ausführung beendet!")
    except FileNotFoundError:
        safe_print(f"❌ Fehler: Datei '{file_path}' nicht gefunden!")
        sys.exit(1)
    except Exception as e:
        safe_print(f"❌ Fehler bei der Ausführung: {e}")
        sys.exit(1)

def repl_command():
    """Startet eine interaktive GerLang-Shell"""
    safe_print("GerLang REPL (Read-Eval-Print-Loop)")
    safe_print("Gib 'ENDE' ein zum Beenden\n")

    def get_repl_tip(msg, user_input):
        msg_lower = msg.lower()
        if "unexpected token" in msg_lower:
            return "Hinweis: Unerwartetes Token. Prüfe die Syntax."
        if "expected ';'" in msg_lower or "expected '}'" in msg_lower or "block" in msg_lower:
            return "Hinweis: Es fehlt vermutlich ein Semikolon oder eine schließende Klammer."
        if "type" in msg_lower or "typ" in msg_lower:
            return "Hinweis: Typfehler. Prüfe die Typen deiner Variablen."
        return "Hinweis: Prüfe die Syntax und den Kontext der Fehlermeldung."

    while True:
        try:
            user_input = input("gerlang> ")

            if user_input.strip().upper() in ['ENDE', 'EXIT', 'QUIT']:
                safe_print("Auf Wiedersehen! 👋")
                break

            if user_input.strip() == '':
                continue

            lexer = Lexer(user_input)
            tokens = lexer.tokenize()
            parser = Parser(tokens)
            try:
                program = parser.parse()
            except Exception as e:
                import re
                msg = str(e)
                m = re.search(r'line (\d+)', msg)
                line = int(m.group(1)) if m else 1
                col = 1
                code_line = user_input
                marker = ' ' * (col-1) + '~~~ FEHLER! ~~~'
                safe_print(f"Fehler beim Parsen in Zeile {line}: {msg}")
                safe_print(f"{line} {code_line}")
                safe_print(f"   {marker}")
                safe_print(get_repl_tip(msg, user_input))
                continue
            interpreter = Interpreter()
            try:
                interpreter.interpret(program)
            except Exception as e:
                msg = str(e)
                safe_print(f"Laufzeitfehler: {msg}")
                safe_print("Tipp: Vielleicht hilft ein Neustart oder ein Blick ins Handbuch.")
        except KeyboardInterrupt:
            safe_print("\nAuf Wiedersehen! 👋")
            break
        except Exception as e:
            safe_print(f"❌ Fehler: {e}")

def info_command():
    """Zeigt Informationen über GerLang"""
    safe_print("📚 GerLang - Die deutsche Programmiersprache")
    safe_print("\nUnterstützte Keywords:")
    from tokens import KEYWORDS

    for german, english in KEYWORDS.items():
        safe_print(f"  {german:<12} -> {english}")

    safe_print(f"\nDateierweiterung: .gerl")
    safe_print(f"Version: 4.1.0 (release)")

def main():
    parser = argparse.ArgumentParser(
        description="🥨 GerLang - Die deutsche Programmiersprache",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Beispiele:
  gerlang run beispiele/haupt.gerl     # Führe eine .gerl Datei aus
  gerlang lex beispiele/haupt.gerl     # Zeige nur die Lexer-Tokens
  gerlang repl                        # Starte interaktive Shell
  gerlang info                        # Zeige Sprachinfos
        """
    )

    subparsers = parser.add_subparsers(dest='command', help='Verfügbare Befehle')

    # run command
    run_parser = subparsers.add_parser('run', help='Führe eine GerLang-Datei aus')
    run_parser.add_argument('file', help='Pfad zur .gerl Datei')

    # lex command
    lex_parser = subparsers.add_parser('lex', help='Zeige Lexer-Tokens einer Datei')
    lex_parser.add_argument('file', help='Pfad zur .gerl Datei')
    lex_parser.add_argument('-v', '--verbose', action='store_true', help='Zeige auch den Quellcode')

    # repl command
    subparsers.add_parser('repl', help='Starte interaktive GerLang-Shell')

    # info command
    subparsers.add_parser('info', help='Zeige Informationen über GerLang')

    args = parser.parse_args()

    # Banner anzeigen
    print_banner()

    if args.command == 'run':
        run_command(args.file)
    elif args.command == 'lex':
        lexer_command(args.file, args.verbose)
    elif args.command == 'repl':
        repl_command()
    elif args.command == 'info':
        info_command()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()