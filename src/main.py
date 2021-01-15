import sys

'''Necessary imports to use the PDL-Procesator'''
from src.analizador_lexico.js_lexer import JSLexer
from src.analizador_sintactico_y_semantico.js_parser import JSParser
from src.tabla_simbolos.sym_table import SymTable

'''Output files where we can see the different results of our input'''
tokens_file = open("Tokens.txt", "w")
parse_file = open("Parse.txt", "w")
TS_file = open("TS-Output.txt", "w")
sys.stderr = open("Error.txt", "w")

'''The input where we obtain the program to analize'''
f = open('Input.txt', 'r')
data = f.read()

'''Global variables to share between the lexer and the parser'''
symbol_table = SymTable()
declaration_scope = [False]
declarando_funcion = [False]
global_shift = [0]

'''Instantiation of both modules'''
lexer = JSLexer(symbol_table, declaration_scope, tokens_file, declarando_funcion, global_shift)
rule_list = []
parser = JSParser(rule_list, symbol_table, declaration_scope, declarando_funcion, global_shift)
parser.parse(lexer.get_token(data))

print(f"Ascendente {str(rule_list).strip('[]').replace(',', '')}", file=parse_file)
symbol_table.write_table(TS_file)
