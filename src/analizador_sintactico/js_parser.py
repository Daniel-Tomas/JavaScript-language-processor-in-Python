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
        return

    @_('B P')
    def P(self, p):
        self.lista_reglas.append(2)
        return

    @_('F P')
    def P(self,p):
        self.lista_reglas.append(3)
        return

    @_('')
    def P(self, p):
        self.lista_reglas.append(4)
        return

    @_('IF ABREPAR E CIERRAPAR S')
    def B(self, p):
        self.lista_reglas.append(5)
        return

    @_('LET T ID PUNTOYCOMA')
    def B(self, p):
        self.lista_reglas.append(6)
        return

    @_('S')
    def B(self, p):
        self.lista_reglas.append(7)
        return

    @_('FOR ABREPAR D PUNTOYCOMA E PUNTOYCOMA Z CIERRAPAR ABRELLAVE C CIERRALLAVE')
    def B(self, p):
        self.lista_reglas.append(8)
        return

    @_('ID OPASIG E PUNTOYCOMA')
    def S(self, p):
        self.lista_reglas.append(9)
        return

    @_('ID ABREPAR L CIERRAPAR PUNTOYCOMA')
    def S(self, p):
        self.lista_reglas.append(10)
        return

    @_('ALERT ABREPAR E CIERRAPAR PUNTOYCOMA')
    def S(self, p):
        self.lista_reglas.append(11)
        return

    @_('INPUT ABREPAR ID CIERRAPAR PUNTOYCOMA')
    def S(self, p):
        self.lista_reglas.append(12)
        return

    @_('RETURN X PUNTOYCOMA')
    def S(self, p):
        self.lista_reglas.append(13)
        return

    @_('NUMBER')
    def T(self, p):
        self.lista_reglas.append(14)
        return

    @_('BOOLEAN')
    def T(self, p):
        self.lista_reglas.append(15)
        return

    @_('STRING')
    def T(self, p):
        self.lista_reglas.append(16)
        return

    @_('F1 F2 F3')
    def F(self, p):
        self.lista_reglas.append(17)
        return

    @_('FUNCTION H ID')
    def F1(self, p):
        self.lista_reglas.append(18)
        return

    @_('ABREPAR A CIERRAPAR')
    def F2(self, p):
        self.lista_reglas.append(19)
        return

    @_('ABRELLAVE C CIERRALLAVE')
    def B(self, p):
        self.lista_reglas.append(20)
        return

    @_('E OPLOG R')
    def E(self, p):
        self.lista_reglas.append(21)
        return

    @_('R')
    def E(self, p):
        self.lista_reglas.append(22)
        return

    @_('R OPREL U')
    def R(self, p):
        self.lista_reglas.append(23)
        return

    @_('U')
    def R(self, p):
        self.lista_reglas.append(24)
        return

    @_('U OPARIT V')
    def U(self, p):
        self.lista_reglas.append(25)
        return

    # TODO: A LAS 19:00 COMENTAR EL POR QUÉ DE LA UNIFICACIÓN DE 25 Y 26 EN 25 (DEJA DE SER AFD)

    @_('V')
    def U(self, p):
        self.lista_reglas.append(27)
        return

    @_('OPESP ID')
    def V(self, p):
        self.lista_reglas.append(28)
        return

    @_('ID')
    def V(self, p):
        self.lista_reglas.append(29)
        return

    @_('ABREPAR E CIERRAPAR')
    def V(self, p):
        self.lista_reglas.append(30)
        return

    @_('ID ABREPAR L CIERRAPAR')
    def V(self, p):
        self.lista_reglas.append(31)
        return

    @_('CTEENTERA')
    def V(self, p):
        self.lista_reglas.append(32)
        return

    @_('CADENA')
    def V(self, p):
        self.lista_reglas.append(33)
        return

    @_('CTELOGICA')
    def V(self, p):
        self.lista_reglas.append(34)
        return

    @_('S')
    def B(self, p):
        self.lista_reglas.append(7)
        return

    @_('S')
    def B(self, p):
        self.lista_reglas.append(7)
        return

    @_('S')
    def B(self, p):
        self.lista_reglas.append(7)
        return

    @_('S')
    def B(self, p):
        self.lista_reglas.append(7)
        return

    @_('S')
    def B(self, p):
        self.lista_reglas.append(7)
        return

    @_('S')
    def B(self, p):
        self.lista_reglas.append(7)
        return

    @_('S')
    def B(self, p):
        self.lista_reglas.append(7)
        return

    @_('S')
    def B(self, p):
        self.lista_reglas.append(7)
        return

    @_('S')
    def B(self, p):
        self.lista_reglas.append(7)
        return

    @_('S')
    def B(self, p):
        self.lista_reglas.append(7)
        return

    @_('S')
    def B(self, p):
        self.lista_reglas.append(7)
        return

    @_('S')
    def B(self, p):
        self.lista_reglas.append(7)
        return

    @_('S')
    def B(self, p):
        self.lista_reglas.append(7)
        return

    @_('S')
    def B(self, p):
        self.lista_reglas.append(7)
        return

    @_('S')
    def B(self, p):
        self.lista_reglas.append(7)
        return

    @_('S')
    def B(self, p):
        self.lista_reglas.append(7)
        return

    @_('S')
    def B(self, p):
        self.lista_reglas.append(7)
        return

    @_('S')
    def B(self, p):
        self.lista_reglas.append(7)
        return

    @_('S')
    def B(self, p):
        self.lista_reglas.append(7)
        return

    @_('S')
    def B(self, p):
        self.lista_reglas.append(7)
        return

    @_('S')
    def B(self, p):
        self.lista_reglas.append(7)
        return

    @_('S')
    def B(self, p):
        self.lista_reglas.append(7)
        return

    @_('S')
    def B(self, p):
        self.lista_reglas.append(7)
        return

    @_('S')
    def B(self, p):
        self.lista_reglas.append(7)
        return

    @_('S')
    def B(self, p):
        self.lista_reglas.append(7)
        return

    @_('S')
    def B(self, p):
        self.lista_reglas.append(7)
        return

    @_('S')
    def B(self, p):
        self.lista_reglas.append(7)
        return

    @_('S')
    def B(self, p):
        self.lista_reglas.append(7)
        return

    @_('S')
    def B(self, p):
        self.lista_reglas.append(7)
        return

    @_('S')
    def B(self, p):
        self.lista_reglas.append(7)
        return

    @_('S')
    def B(self, p):
        self.lista_reglas.append(7)
        return

    @_('S')
    def B(self, p):
        self.lista_reglas.append(7)
        return

    @_('S')
    def B(self, p):
        self.lista_reglas.append(7)
        return
