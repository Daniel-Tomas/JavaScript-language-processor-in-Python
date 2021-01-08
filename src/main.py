import sys

from src.analizador_lexico.js_lexer import JSLexer
from src.analizador_semantico.js_parser import JSParser
from src.tabla_simbolos.sym_table import SymTable

tokens_file = open("Tokens.txt", "w")
parse_file = open("Parse.txt", "w")
TS_file = open("TS-Output.txt", "w")
sys.stderr = open("Error.txt", "w")

f = open('Input.txt', 'r')
data = f.read()

symbol_table = SymTable()
declaration_scope = [False]
declarando_funcion = [False]
global_shift = [0]

lexer = JSLexer(symbol_table, declaration_scope, tokens_file, declarando_funcion, global_shift)

listaReglas = []
parser = JSParser(listaReglas, symbol_table, declaration_scope, declarando_funcion, global_shift)

parser.parse(lexer.get_token(data))

print(f"Ascendente {str(listaReglas).strip('[]').replace(',', '')}", file=parse_file)
symbol_table.write_table(TS_file)
