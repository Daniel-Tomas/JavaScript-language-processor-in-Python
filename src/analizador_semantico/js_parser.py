import sys
from collections import deque

from sly import Parser

from src.analizador_lexico.js_lexer import JSLexer
from src.tabla_simbolos.sym_table import SymTable


class JSParser(Parser):
    debugfile = 'parser.out'

    tokens = JSLexer.tokens

    def __init__(self, lista_reglas_, TS_, declaration_scope_):
        self.lista_reglas = lista_reglas_
        self.TS = TS_
        self.TS.new_table()
        self.desp = 0
        self.declaration_scope = declaration_scope_
        self.declaration_scope[0] = True

        self.atrib_stack = deque()

    @_('D')
    def B(self, p):
        self.lista_reglas.append(1)
        return

    @_('F D')
    def D(self, p):
        self.lista_reglas.append(2)
        return

    @_('G D')
    def D(self, p):
        self.lista_reglas.append(3)
        return

    @_('')
    def D(self, p):
        self.lista_reglas.append(4)
        return

    @_('IF ABPAREN E CEPAREN S')
    def G(self, p):
        type = self.atrib_stack.pop()
        if type != 'log':
            self.sem_error(1)
        self.lista_reglas.append(5)
        return

    @_('S')
    def G(self, p):
        self.lista_reglas.append(6)
        return

    @_('H PUNTOYCOMA')
    def S(self, p):
        self.lista_reglas.append(7)
        return

    @_('ID ABPAREN I CEPAREN')
    def H(self, p):
        types = self.atrib_stack.pop()
        if len(types) != self.TS.get_attribute(p.ID.TS_index, p.ID.value, "num_params"):
            self.sem_error(2)
        # for comparar tipos
        self.atrib_stack.append("busca_tipo_devuelto_TS(id.pos)")
        self.lista_reglas.append(8)
        return

    @_('E J')
    def I(self, p):
        self.lista_reglas.append(9)
        return

    @_('COMA E J')
    def J(self, p):
        self.lista_reglas.append(10)
        return

    @_('')
    def J(self, p):
        self.lista_reglas.append(11)
        return

    @_('')
    def I(self, p):
        self.lista_reglas.append(12)
        return

    @_('K PUNTOYCOMA')
    def S(self, p):
        self.lista_reglas.append(13)
        return

    @_('ID OPASIG E')
    def K(self, p):
        self.lista_reglas.append(14)
        return

    @_('ALERT ABPAREN E CEPAREN PUNTOYCOMA')
    def S(self, p):
        self.lista_reglas.append(15)
        return

    @_('INPUT ABPAREN ID CEPAREN PUNTOYCOMA')
    def S(self, p):
        self.lista_reglas.append(16)
        return

    @_('RETURN L PUNTOYCOMA')
    def S(self, p):
        self.lista_reglas.append(17)
        return

    @_('E')
    def L(self, p):
        self.lista_reglas.append(18)
        return

    @_('')
    def L(self, p):
        self.lista_reglas.append(19)
        return

    @_('LET M T ID PUNTOYCOMA')
    def G(self, p):
        self.declaration_scope[0] = False
        self.TS.add_attribute(p.ID[0], p.ID[1], 'Tipo', p.T[0])
        self.TS.add_attribute(p.ID[0], p.ID[1], 'Desp', self.desp)
        self.desp += p.T[1]

        self.lista_reglas.append(20)
        return

    @_('')
    def M(self, p):
        self.declaration_scope[0] = True
        self.lista_reglas.append(21)
        return

    @_('NUMBER')
    def T(self, p):
        self.lista_reglas.append(22)
        return

    @_('BOOLEAN')
    def T(self, p):
        self.lista_reglas.append(23)
        return

    @_('STRING')
    def T(self, p):
        self.lista_reglas.append(24)
        return 'cadena', 128

    @_('FOR ABPAREN N PUNTOYCOMA E PUNTOYCOMA O CEPAREN ABLLAVE C CELLAVE')
    def G(self, p):
        self.lista_reglas.append(25)
        return

    @_('K')
    def N(self, p):
        self.lista_reglas.append(26)
        return

    @_('')
    def N(self, p):
        self.lista_reglas.append(27)
        return

    @_('K')
    def O(self, p):
        self.lista_reglas.append(28)
        return

    @_('OPESP ID')
    def O(self, p):
        self.lista_reglas.append(29)
        return

    @_('')
    def O(self, p):
        self.lista_reglas.append(30)
        return

    @_('G C')
    def C(self, p):
        self.lista_reglas.append(31)
        return

    @_('')
    def C(self, p):
        self.lista_reglas.append(32)
        return

    @_('F1 F2 F3')
    def F(self, p):
        self.lista_reglas.append(33)
        return

    @_('FUNCTION P Q ID')
    def F1(self, p):
        self.lista_reglas.append(34)
        return

    @_('')
    def P(self, p):
        self.lista_reglas.append(35)
        return

    @_('T')
    def Q(self, p):
        self.lista_reglas.append(36)
        return

    @_('')
    def Q(self, p):
        self.lista_reglas.append(37)
        return

    @_('ABPAREN A CEPAREN')
    def F2(self, p):
        self.lista_reglas.append(38)
        return

    @_('T ID R')
    def A(self, p):
        self.lista_reglas.append(39)
        return

    @_('')
    def A(self, p):
        self.lista_reglas.append(40)
        return

    @_('COMA T ID R')
    def R(self, p):
        self.lista_reglas.append(41)
        return

    @_('')
    def R(self, p):
        self.lista_reglas.append(42)
        return

    @_('ABLLAVE C CELLAVE')
    def F3(self, p):
        self.lista_reglas.append(43)
        return

    @_('E OPLOG R')
    def E(self, p):
        self.lista_reglas.append(44)
        return

    @_('R')
    def E(self, p):
        self.lista_reglas.append(45)
        return

    @_('R OPREL U')
    def R(self, p):
        self.lista_reglas.append(46)
        return

    @_('U')
    def R(self, p):
        self.lista_reglas.append(47)
        return

    @_('U OPARIT V')
    def U(self, p):
        self.lista_reglas.append(48)
        return

    @_('V')
    def U(self, p):
        self.lista_reglas.append(49)
        return

    @_('OPESP ID')
    def V(self, p):
        self.lista_reglas.append(50)
        return

    @_('ID')
    def V(self, p):
        self.lista_reglas.append(51)
        return

    @_('ABPAREN E CEPAREN')
    def V(self, p):
        self.lista_reglas.append(52)
        return

    @_('H')
    def V(self, p):
        self.lista_reglas.append(53)
        return

    @_('CTEENTERA')
    def V(self, p):
        self.lista_reglas.append(54)
        return

    @_('CADENA')
    def V(self, p):
        self.lista_reglas.append(55)
        return

    @_('CTELOGICA')
    def V(self, p):
        self.lista_reglas.append(56)
        return

    def error(self, p):
        res = str(self.lista_reglas).strip('[]')
        res = res.replace(',', '')
        print(f'Ascendente {res}', file=sys.stderr)
        print("Error sintáctico: ", file=sys.stderr)
        if not p:
            print("End of File!", file=sys.stderr)
            exit(2)
        else:
            print(f'Token ilegal {p.type} en la linea {p.lineno}', file=sys.stderr)
            exit(3)

    def sem_error(self, id):
        pass


if __name__ == '__main__':
    sys.stdout = open("Parse.txt", "w")
    sys.stderr = open("Error.txt", "w")

    tables = SymTable()
    id0 = tables.new_table()
    listaReglas = []

    lexer = JSLexer(tables)
    parser = JSParser(listaReglas, tables)
    f = open('Input.txt', 'r')
    data = f.read()
    result = parser.parse(lexer.get_token(data))
    res = str(listaReglas).strip('[]')
    res = res.replace(',', '')
    print(f'Ascendente {res}')
    tables.write_table("TS-Output.txt")
