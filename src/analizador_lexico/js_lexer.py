from sly import Lexer
from sly.lex import Token
from src.tabla_simbolos.sym_table import SymTable
import sys


class JSLexer(Lexer):
    """Represents a javascript lexer."""

    # Args:
    #     data (str): the text to be set.
    #
    # Attributes:
    #     data (str): the code which is going to be analyzed by the lexer.
    #
    # """
    #
    def __init__(self, ts_, declaration_scope_, tokens_file_, declarando_funcion_, global_shift_):
        self.ts = ts_
        self.declaration_scope = declaration_scope_
        self.tokens_file = tokens_file_
        self.declarando_funcion = declarando_funcion_
        self.global_shift = global_shift_

    tokens = {CTEENTERA, CADENA, CTELOGICA, OPARIT, OPESP,
              OPREL, OPLOG, OPASIG, ID, NUMBER, STRING, BOOLEAN, LET, ALERT,
              INPUT, FUNCTION, ABPAREN, CEPAREN, ABLLAVE, CELLAVE, COMA,
              PUNTOYCOMA, RETURN, IF, FOR
              }

    ignore = ' \t'

    # Tokens
    CTEENTERA = r'\d+'
    CADENA = r'".*?"'
    CTELOGICA = r'true|false'
    OPESP = r'--'
    OPARIT = r'-'
    OPREL = r'=='
    OPASIG = r'='
    OPLOG = r'&&'

    ABPAREN = r'\('
    CEPAREN = r'\)'
    ABLLAVE = r'\{'
    CELLAVE = r'\}'
    COMA = r','
    PUNTOYCOMA = r';'

    ID = r'[a-zA-Z][a-zA-Z0-9_]*'

    ID['number'] = NUMBER
    ID['string'] = STRING
    ID['boolean'] = BOOLEAN
    ID['let'] = LET
    ID['alert'] = ALERT
    ID['input'] = INPUT
    ID['function'] = FUNCTION
    ID['return'] = RETURN
    ID['if'] = IF
    ID['for'] = FOR

    def empty(self, t):
        t.value = ''
        return t

    def OPESP(self, t):
        return self.empty(t)

    def OPARIT(self, t):
        return self.empty(t)

    def OPREL(self, t):
        return self.empty(t)

    def OPASIG(self, t):
        return self.empty(t)

    def OPLOG(self, t):
        return self.empty(t)

    def ABPAREN(self, t):
        return self.empty(t)

    def CEPAREN(self, t):
        return self.empty(t)

    def ABLLAVE(self, t):
        return self.empty(t)

    def CELLAVE(self, t):
        return self.empty(t)

    def COMA(self, t):
        return self.empty(t)

    def PUNTOYCOMA(self, t):
        return self.empty(t)

    @_(r'[a-zA-Z][a-zA-Z0-9_]*')
    def NUMBER(self, t):
        return self.empty(t)

    @_(r'[a-zA-Z][a-zA-Z0-9_]*')
    def STRING(self, t):
        return self.empty(t)

    @_(r'[a-zA-Z][a-zA-Z0-9_]*')
    def BOOLEAN(self, t):
        return self.empty(t)

    @_(r'[a-zA-Z][a-zA-Z0-9_]*')
    def LET(self, t):
        return self.empty(t)

    @_(r'[a-zA-Z][a-zA-Z0-9_]*')
    def ALERT(self, t):
        return self.empty(t)

    @_(r'[a-zA-Z][a-zA-Z0-9_]*')
    def INPUT(self, t):
        return self.empty(t)

    @_(r'[a-zA-Z][a-zA-Z0-9_]*')
    def FUNCTION(self, t):
        self.declarando_funcion[0] = True
        return self.empty(t)

    @_(r'[a-zA-Z][a-zA-Z0-9_]*')
    def RETURN(self, t):
        return self.empty(t)

    @_(r'[a-zA-Z][a-zA-Z0-9_]*')
    def IF(self, t):
        return self.empty(t)

    @_(r'[a-zA-Z][a-zA-Z0-9_]*')
    def FOR(self, t):
        return self.empty(t)

    def CTEENTERA(self, t):
        """ If the number found is bigger than 32767 calls self.lex_error.

        Casts the token values from str to int.

        Args:
            t(Token): The integer constant token.

        Returns:
            Token: The token modified.
        """

        t.value = int(t.value)
        if t.value > 32767:
            self.lex_error(t, "CTEENTERA")
        return t

    def CTELOGICA(self, t):
        """Modifies the argument token changing its str value
            to an integer value.

        The token value is set 0 if "false" is found or 1 if "true"

        Args:
            t(Token): Token which matches the logical constant pattern

        Returns:
            Token: Token modified
        """

        if t.value == 'false':
            t.value = 0
        else:
            t.value = 1
        return t

    def CADENA(self, t):
        """If the string length is bigger than 64 calls self.lex_error.

        Args:
            t(Token): The string constant token.

        Returns:
            Token: the same token.
        """
        if len(t.value) > 64:
            self.lex_error(t, "CADENA")
        return t

    def ID(self, t):
        if self.declarando_funcion[0]:
            self.declaration_scope[0] = True
            id_table, id_pos = self.ts.get_local_pos(t.value)
        else:
            id_table, id_pos = self.ts.get_pos(t.value)

        if self.declaration_scope[0]:
            if id_table is not None:
                self.lex_error(t, 'ID')
            else:
                id_table, id_pos = self.ts.add_entry(t.value)
                t.value = (id_table, id_pos)

            self.declaration_scope[0] = False

        else:
            if id_table is None:
                id_table, id_pos = self.ts.add_global_entry(t.value)
                self.ts.add_attribute(id_table, id_pos, 'Tipo', 'entero')
                self.ts.add_attribute(id_table, id_pos, 'Despl', self.global_shift[0])
                self.global_shift[0] += 2
                t.value = (id_table, id_pos)
            else:
                t.value = (id_table, id_pos)

        return t

    @_('\n+',
       r'(?s:/\*.*?\*/)')
    def new_line(self, t):
        """Increases the line number.

        Increases the line number where the lexer is working to provide a
         correct information when a lex_error is found.

        Args:
            t(Token): The token which contains_lex a comment or a newline.
        """
        self.lineno += t.value.count('\n')

    def find_column(self, token):
        """Finds the column where the first letter of a token is placed.

        Args:
            token(Token): The only parameter.
        """
        last_cr = self.text.rfind('\n', 0, token.index)
        if last_cr < 0:
            last_cr = 0
        column = (token.index - last_cr)
        return column

    def lex_error(self, t, type_error="default"):
        """Handles lexer errors.

        A lex_error is reported when a wrong character is found.
        Prints a description of the lex_error and provides the number of the
         line and the column where it has been found.
        **Particular errors**:
            1. Value of a token which type is "CADENA" has a length
             greater than 64
            2. Value of a token which type is "CTE_ENTERA" is bigger
             than 32767

        Args:
            t(Token): The only parameter.
        """

        res = f'Error en la linea {self.lineno} y columna {self.find_column(t)}:\n\t'
        if type_error == 'CADENA':
            res += f'Cadena demasiado larga: "{t.value}", con logitud mayor que 64: {len(t.value)},'
        elif type_error == "CTEENTERA":
            res += f'Número fuera de rango: "{t.value},"'
        elif type_error == 'ID':
            res += f'Identificador ya declarado: "{t.value},"'
        else:
            res += f'Carácter ilegal: "{t.value[0]}"'

        print(res, file=sys.stderr)
        exit(1)

    def get_token(self, data):
        """Generator that yields tokens of the data text one by one and prints them.

        Yields:
            Token: The next token.
        """
        for tok in self.tokenize(data):
            if tok.type == "ID":
                print(f'<{tok.type} , {tok.value[1]}>', file=self.tokens_file)
            else:
                print(f'<{tok.type} , {tok.value}>', file=self.tokens_file)
            yield tok


if __name__ == '__main__':

    sys.stdout = open("Tokens.txt", "w")
    sys.stderr = open("Error.txt", "w")

    f = open('Input.txt', 'r')
    data = f.read()

    tables = SymTable()
    id0 = tables.new_table()
    lexer = JSLexer(tables)

    for tok in lexer.tokenize(data):
        print(f'<{tok.type} , {tok.value}>')
    tables.write_table("TS-Output.txt")
