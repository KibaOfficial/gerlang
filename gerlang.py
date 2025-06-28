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

def print_banner():
    """Zeigt das GerLang Banner"""
    print("GerLang - Die deutsche Programmiersprache")
    print("=" * 50)

def lexer_command(file_path: str, verbose: bool = False):
    """Führt nur den Lexer aus und zeigt die Tokens"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            source_code = f.read()

        if verbose:
            print(f"📄 Datei: {file_path}")
            print("📝 Quellcode:")
            print("-" * 30)
            print(source_code)
            print("-" * 30)

        lexer = Lexer(source_code)
        tokens = lexer.tokenize()

        print("\n🔍 Lexer-Analyse:")
        print("-" * 50)

        for token in tokens:
            if token.type == "EOF":
                print(f"{'EOF':<15} | {'<end>':<20} | Line {token.line:>2}, Col {token.column:>2}")
            else:
                # Kürze lange Values für bessere Darstellung
                display_value = token.value[:20] + "..." if len(token.value) > 20 else token.value
                print(f"{token.type:<15} | {display_value:<20} | Line {token.line:>2}, Col {token.column:>2}")

        print(f"\n✅ Lexer erfolgreich! {len(tokens)} Tokens erkannt.")

    except FileNotFoundError:
        print(f"❌ Fehler: Datei '{file_path}' nicht gefunden!")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Lexer-Fehler: {e}")
        sys.exit(1)

def run_command(file_path: str):
    """Führt eine GerLang-Datei aus (jetzt mit Parser & Interpreter!)"""
    print(f"🚀 Führe {file_path} aus...")

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
        parser = Parser(tokens)
        try:
            program = parser.parse()
        except Exception as e:
            import traceback
            tb = traceback.extract_tb(e.__traceback__)
            token = getattr(e, 'token', None)
            if hasattr(e, 'args') and e.args:
                msg = e.args[0]
            else:
                msg = str(e)
            import re
            m = re.search(r'line (\d+)', msg)
            line = int(m.group(1)) if m else '?'
            col = getattr(token, 'column', '?') if token else '?'
            code_lines = source_code.splitlines()
            code_line = code_lines[line-1] if isinstance(line, int) and line != '?' and 1 <= line <= len(code_lines) else ''
            marker = ' ' * (col-1 if isinstance(col, int) and col != '?' else 0) + '~~~ FEHLER! ~~~'
            print(f"\n{file_path}:{line}:{col} - Fehler G42: {msg}")
            print(f"\n{line} {code_line}")
            print(f"   {marker}")
            print(get_humorous_tip(msg))
            sys.exit(2)
        interpreter = Interpreter()
        try:
            interpreter.interpret(program)
        except Exception as e:
            import traceback
            msg = str(e)
            tb = traceback.extract_tb(e.__traceback__)
            # Versuche Zeile/Spalte zu finden (optional, falls Interpreter das liefert)
            line = getattr(e, 'line', '?')
            col = getattr(e, 'column', '?')
            print(f"\n{file_path}:{line}:{col} - Laufzeitfehler: {msg}")
            print("Tipp: Vielleicht hast du eine Variable vergessen, einen Typen verwechselt oder die Wurst zu früh gegessen.")
            sys.exit(3)
        print("\n✅ Ausführung beendet!")
    except FileNotFoundError:
        print(f"❌ Fehler: Datei '{file_path}' nicht gefunden!")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Fehler bei der Ausführung: {e}")
        sys.exit(1)

def repl_command():
    """Startet eine interaktive GerLang-Shell"""
    print("GerLang REPL (Read-Eval-Print-Loop)")
    print("Gib 'ENDE' ein zum Beenden\n")

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
                print("Auf Wiedersehen! 👋")
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
                print(f"Fehler beim Parsen in Zeile {line}: {msg}")
                print(f"{line} {code_line}")
                print(f"   {marker}")
                print(get_repl_tip(msg, user_input))
                continue
            interpreter = Interpreter()
            try:
                interpreter.interpret(program)
            except Exception as e:
                msg = str(e)
                print(f"Laufzeitfehler: {msg}")
                print("Tipp: Vielleicht hilft ein Neustart oder ein Blick ins Handbuch.")
        except KeyboardInterrupt:
            print("\nAuf Wiedersehen! 👋")
            break
        except Exception as e:
            print(f"❌ Fehler: {e}")

def info_command():
    """Zeigt Informationen über GerLang"""
    print("📚 GerLang - Die deutsche Programmiersprache")
    print("\nUnterstützte Keywords:")
    from tokens import KEYWORDS

    for german, english in KEYWORDS.items():
        print(f"  {german:<12} -> {english}")

    print(f"\nDateierweiterung: .gerl")
    print(f"Version: 3.0.0 (release)")

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