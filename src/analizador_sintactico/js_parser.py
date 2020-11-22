from sly import Parser
from src.analizador_lexico.js_lexer import JSLexer
from src.tabla_simbolos.sym_table import SymTable
import sys


class JSParser(Parser):
    debugfile = 'parser.out'

    def __init__(self, lista_reglas_, TS_):
        self.lista_reglas = lista_reglas_
        self.TS = TS_

    @_('P')
    def Y(self, p):
        self.lista_reglas.append(1)
        return p.P

    @_('P')
    def Y(self, p):
        self.lista_reglas.append(1)
        return p.P
