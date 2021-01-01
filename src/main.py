import sys

from src.analizador_lexico.js_lexer import JSLexer
from src.analizador_semantico.js_parser import JSParser
from src.tabla_simbolos.sym_table import SymTable

if __name__ == '__main__':
    tokens_file = open("Tokens.txt", "w")
    parse_file = open("Parse.txt", "w")
    TS_file = open("TS-Output.txt", "w")
    #sys.stderr = open("Error.txt", "w")

    symbol_table = SymTable()
    declaration_scope = [False]


    lexer = JSLexer(symbol_table, declaration_scope, tokens_file)

    listaReglas = []
    parser = JSParser(listaReglas, symbol_table, declaration_scope)

    f = open('Input.txt', 'r')
    data = f.read()
    result = parser.parse(lexer.get_token(data))

    res = str(listaReglas).strip('[]')
    res = res.replace(',', '')
    print(f'Ascendente {res}', file=parse_file)
    symbol_table.write_table(TS_file)
