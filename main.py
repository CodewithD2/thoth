from Lexer import Lexer
from Parser import Parser
from AST import Program
import json


LEXER_DEBUG : bool = False
PARSER_DEBUG : bool = True


if __name__ == '__main__':
    with open ("tests/parser.th" , "r") as f:
        code: str =f.read()

    if LEXER_DEBUG:
        debug_lex : Lexer = Lexer(source=code)

        while debug_lex.current_char is not None:
            print(debug_lex.next_token())    

    l : Lexer = Lexer(source=code)
    p : Parser = Parser(lexer=l)

    if PARSER_DEBUG:
        print("===== Parser Debug =====")
        program : Program = p.parse_program()

        with open("debug/ast.json" , "w" ) as f:
            json.dump(program.json() , f, indent=4)

        print("Ast json file created successfully")
