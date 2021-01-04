import sys

from sly import Parser

from src.analizador_lexico.js_lexer import JSLexer


class JSParser(Parser):
    ATTR_TYPE = 'Tipo'
    ATTR_DESP = 'Despl'
    ATTR_NUM_PARAMS = 'numParam'
    ATTR_TYPE_PARAMS = 'TipoParam'
    ATTR_RETURN_VALUE = 'TipoRetorno'

    FUNCTION_TYPE = 'función'
    LOG_TYPE = 'lógico'
    INT_TYPE = 'entero'
    STRING_TYPE = 'cadena'
    VOID_TYPE = 'void'

    error_code_dict = {
        1: "La condición debe ser un lógico",
        2: "El número de parámetros introducidos no son los esperados, deberían ser {busca_num_params_TS(id.pos)}",
        3: "El tipo de los parámetros no es el esperado, se esperaban {busca_tipo_params_TS(id.pos)}",
        4: "La expresión introducida no es una cadena o un entero",
        5: "La variable introducida no es de tipo cadena o entero",
        6: "La condición debe ser un lógico",
        7: "No puede haber return fuera de una función",
        8: "No se permite la definición de funciones anidadas",
        9: "El tipo de retorno no corresponde con el tipo de retorno de la función, se esperaba {tipo_return}",
        10: "El tipo de la variable a asignar no corresponde con el tipo asignado",
        11: "El operador especial '--' solo trabaja con tipos de datos enteros",
        12: "El operador lógico '&&' solo trabaja con tipos de datos lógicos",
        13: "El operador de relación '==' solo trabaja con tipos de datos enteros",
        14: "El operador aritmético '-' solo trabaja con tipos de datos enteros",
        15: "La variable no se puede invocar como una función, con argumentos"
    }

    debugfile = 'parser.out'
    tokens = JSLexer.tokens

    def __init__(self, lista_reglas_, TS_, declaration_scope_, declarando_funcion_, global_shift_):
        self.lista_reglas = lista_reglas_
        self.TS = TS_
        self.TS.new_table()
        self.shift = 0
        self.declaration_scope = declaration_scope_
        self.declaration_scope[0] = False
        self.function_scope = False
        self.return_type = None
        self.global_shift = global_shift_
        self.pos_id_fun = None
        self.number_function = 0
        self.declarando_funcion = declarando_funcion_

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
        if p.E != self.LOG_TYPE:
            self.sem_error(1, p.lineo)
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
        if self.TS.get_attribute(p.ID[0], p.ID[1], self.ATTR_TYPE) != self.FUNCTION_TYPE:
            self.sem_error(15, p.lineno)
        if self.TS.get_attribute(p.ID[0], p.ID[1], self.ATTR_NUM_PARAMS) == 0 and p.I == self.VOID_TYPE:
            return self.TS.get_attribute(p.ID[0], p.ID[1], self.ATTR_RETURN_VALUE)
        if self.TS.get_attribute(p.ID[0], p.ID[1], self.ATTR_NUM_PARAMS) != len(p.I):
            self.sem_error(2, p.lineno)
        for index, param in enumerate(self.TS.get_attribute(p.ID[0], p.ID[1], self.ATTR_TYPE_PARAMS)):
            if param != p.I[index]:
                self.sem_error(3, p.lineno)

        self.lista_reglas.append(8)
        return self.TS.get_attribute(p.ID[0], p.ID[1], self.ATTR_RETURN_VALUE)

    @_('E J')
    def I(self, p):
        list = p.J
        list.insert(0, p.E)
        self.lista_reglas.append(9)
        return list

    @_('COMA E J')
    def J(self, p):
        list = p.J
        list.insert(0, p.E)
        self.lista_reglas.append(10)
        return list

    @_('')
    def J(self, p):
        self.lista_reglas.append(11)
        return []

    @_('')
    def I(self, p):
        self.lista_reglas.append(12)
        return self.VOID_TYPE

    @_('K PUNTOYCOMA')
    def S(self, p):
        self.lista_reglas.append(13)
        return

    @_('ID OPASIG E')
    def K(self, p):
        if self.TS.get_attribute(p.ID[0], p.ID[1], self.ATTR_TYPE) != p.E:
            self.sem_error(10, p.lineno)
        self.lista_reglas.append(14)
        return

    @_('ALERT ABPAREN E CEPAREN PUNTOYCOMA')
    def S(self, p):
        if p.E != self.STRING_TYPE and p.E != self.INT_TYPE:
            self.sem_error(4, p)
        self.lista_reglas.append(15)
        return

    @_('INPUT ABPAREN ID CEPAREN PUNTOYCOMA')
    def S(self, p):
        type = self.TS.get_attribute(p.ID[0], p.ID[1], self.ATTR_TYPE)
        if type != self.STRING_TYPE and type != self.INT_TYPE:
            self.sem_error(5, p)
        self.lista_reglas.append(16)
        return

    @_('RETURN L PUNTOYCOMA')
    def S(self, p):
        if not self.function_scope:
            self.sem_error(7, p.lineno)
        if p.L != self.return_type:
            self.sem_error(9, p.lineno)
        self.lista_reglas.append(17)
        return

    @_('E')
    def L(self, p):
        self.lista_reglas.append(18)
        return p.E

    @_('')
    def L(self, p):
        self.lista_reglas.append(19)
        return self.VOID_TYPE

    @_('LET M T ID PUNTOYCOMA')
    def G(self, p):
        self.TS.add_attribute(p.ID[0], p.ID[1], self.ATTR_TYPE, p.T[0])
        self.TS.add_attribute(p.ID[0], p.ID[1], self.ATTR_DESP, self.shift)
        self.shift += p.T[1]
        if not self.function_scope:
            self.global_shift[0] = self.shift
        self.declaration_scope[0] = False
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
        return self.INT_TYPE, 2

    @_('BOOLEAN')
    def T(self, p):
        self.lista_reglas.append(23)
        return self.LOG_TYPE, 2

    @_('STRING')
    def T(self, p):
        self.lista_reglas.append(24)
        return self.STRING_TYPE, 128

    @_('FOR ABPAREN N PUNTOYCOMA E PUNTOYCOMA O CEPAREN ABLLAVE C CELLAVE')
    def G(self, p):
        if p.E != self.LOG_TYPE:
            self.sem_error(6, p.lineno)
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
        if self.TS.get_attribute(p.ID[0], p.ID[1], self.ATTR_TYPE) != self.INT_TYPE:
            self.sem_error(11, p.lineno)
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
        self.TS.destroy_table(len(self.TS.tables) - 1)
        self.function_scope = False
        self.return_type = None
        self.shift = self.global_shift[0]
        self.lista_reglas.append(33)
        return

    @_('FUNCTION P Q ID')
    def F1(self, p):
        self.TS.new_table()
        self.global_shift[0] = self.shift
        self.shift = 0
        self.pos_id_fun = p.ID
        self.function_scope = True

        self.TS.add_attribute(p.ID[0], p.ID[1], self.ATTR_TYPE, self.FUNCTION_TYPE)
        if p.Q == 'void':
            self.return_type = p.Q
            self.TS.add_attribute(p.ID[0], p.ID[1], self.ATTR_RETURN_VALUE, self.VOID_TYPE)
        else:
            self.return_type = p.Q[0]
            self.TS.add_attribute(p.ID[0], p.ID[1], self.ATTR_RETURN_VALUE, p.Q[0])

        self.TS.add_attribute(p.ID[0], p.ID[1], 'EtiqFuncion', 'Et_Fun_' + str(self.number_function))
        self.number_function += 1
        self.lista_reglas.append(34)
        return

    @_('')
    def P(self, p):
        self.lista_reglas.append(35)
        return

    @_('T')
    def Q(self, p):
        self.declaration_scope[0] = True
        self.lista_reglas.append(36)
        return p.T

    @_('')
    def Q(self, p):
        self.declaration_scope[0] = True
        self.lista_reglas.append(37)
        return self.VOID_TYPE

    @_('ABPAREN A CEPAREN')
    def F2(self, p):
        list = p.A
        if list == self.VOID_TYPE:
            self.TS.add_attribute(self.pos_id_fun[0], self.pos_id_fun[1], self.ATTR_NUM_PARAMS, 0)
            self.TS.add_attribute(self.pos_id_fun[0], self.pos_id_fun[1], self.ATTR_TYPE_PARAMS, self.VOID_TYPE)
        else:
            types = []
            for i in range(0, len(list), 2):
                type = list[i]
                pos = list[i + 1]
                self.TS.add_attribute(pos[0], pos[1], self.ATTR_TYPE, type[0])
                self.TS.add_attribute(pos[0], pos[1], self.ATTR_DESP, self.shift)
                self.shift += type[1]
                types.append(type[0])
            self.TS.add_attribute(self.pos_id_fun[0], self.pos_id_fun[1], self.ATTR_NUM_PARAMS, len(types))
            self.TS.add_attribute(self.pos_id_fun[0], self.pos_id_fun[1], self.ATTR_TYPE_PARAMS, types)
        self.declaration_scope[0] = False
        self.declarando_funcion[0] = False
        self.lista_reglas.append(38)
        return

    @_('T ID W')
    def A(self, p):
        list = p.W
        list.insert(0, p.ID)
        list.insert(0, p.T)
        self.lista_reglas.append(39)
        return list

    @_('')
    def A(self, p):
        self.lista_reglas.append(40)
        return self.VOID_TYPE

    @_('COMA T ID W')
    def W(self, p):
        list = p.W
        list.insert(0, p.ID)
        list.insert(0, p.T)
        self.lista_reglas.append(41)
        return list

    @_('')
    def W(self, p):
        self.lista_reglas.append(42)
        return []

    @_('ABLLAVE C CELLAVE')
    def F3(self, p):
        self.lista_reglas.append(43)
        return

    @_('E OPLOG R')
    def E(self, p):
        if p.E != self.LOG_TYPE or p.R != self.LOG_TYPE:
            self.sem_error(12, p.lineno)

        self.lista_reglas.append(44)
        return self.LOG_TYPE

    @_('R')
    def E(self, p):
        self.lista_reglas.append(45)
        return p.R

    @_('R OPREL U')
    def R(self, p):
        if p.R != self.INT_TYPE or p.U != self.INT_TYPE:
            self.sem_error(13, p.lineno)

        self.lista_reglas.append(46)
        return self.LOG_TYPE

    @_('U')
    def R(self, p):
        self.lista_reglas.append(47)
        return p.U

    @_('U OPARIT V')
    def U(self, p):
        if p.U != self.INT_TYPE or p.V != self.INT_TYPE:
            self.sem_error(14, p.lineno)

        self.lista_reglas.append(48)
        return self.INT_TYPE

    @_('V')
    def U(self, p):
        self.lista_reglas.append(49)
        return p.V

    @_('OPESP ID')
    def V(self, p):
        if self.TS.get_attribute(p.ID[0], p.ID[1], self.ATTR_TYPE) != self.INT_TYPE:
            self.sem_error(11, p.lineno)

        self.lista_reglas.append(50)
        return self.INT_TYPE

    @_('ID')
    def V(self, p):
        self.lista_reglas.append(51)
        return self.TS.get_attribute(p.ID[0], p.ID[1], self.ATTR_TYPE)

    @_('ABPAREN E CEPAREN')
    def V(self, p):
        self.lista_reglas.append(52)
        return p.E

    @_('H')
    def V(self, p):
        self.lista_reglas.append(53)
        return p.H

    @_('CTEENTERA')
    def V(self, p):
        self.lista_reglas.append(54)
        return self.INT_TYPE

    @_('CADENA')
    def V(self, p):
        self.lista_reglas.append(55)
        return self.STRING_TYPE

    @_('CTELOGICA')
    def V(self, p):
        self.lista_reglas.append(56)
        return self.LOG_TYPE

    def error(self, p):
        print("Error en la sintaxis: ", file=sys.stderr)
        if not p:
            print("Expresión incompleta, se esperaban más elementos", file=sys.stderr)
            exit(2)
        else:
            print(f'Token ilegal {p.type} en la linea {p.lineno}', file=sys.stderr)
            exit(3)

    def sem_error(self, id, lineno):
        print(f'Error en la linea {lineno}:\n\t{self.error_code_dict[id]}', file=sys.stderr)
        exit(4)

# if __name__ == '__main__':
#     sys.stdout = open("Parse.txt", "w")
#     sys.stderr = open("Error.txt", "w")
#
#     tables = SymTable()
#     id0 = tables.new_table()
#     listaReglas = []
#
#     lexer = JSLexer(tables)
#     parser = JSParser(listaReglas, tables)
#     f = open('Input.txt', 'r')
#     data = f.read()
#     result = parser.parse(lexer.get_token(data))
#     res = str(listaReglas).strip('[]')
#     res = res.replace(',', '')
#     print(f'Ascendente {res}')
#     tables.write_table("TS-Output.txt")
