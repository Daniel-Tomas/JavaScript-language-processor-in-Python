from sly import Lexer
from sly.lex import Token
from pyTable.SymTable import SymTable
import sys


class JSLexer(Lexer):
    """Represents a javascript lexer.

    Args:
        data (str): the text to be set.

    Attributes:
        data (str): the code which is going to be analyzed by the lexer.

    """

    def __init__(self, data):
        self.data = data

    tokens = {CTEENTERA, CADENA, CTELOGICA, OPARIT, OPESP,
              OPREL, OPLOG, OPASIG, ID, NUMBER, STRING, BOOLEAN, LET, ALERT,
              INPUT, FUNCTION, ABPAREN, CEPAREN, ABLLAVE, CELLAVE, COMA, PUNTOYCOMA, RETURN, IF, FOR, EOF}

    ignore = ' \t'

    # Tokens
    CTEENTERA = r'\d+'
    CADENA = r'".*?"'
    CTELOGICA = r'true|false'
    OPESP = r'--'
    OPARIT = r'\+|-'
    OPREL = r'=='
    OPASIG = r'='
    OPLOG = r'&&'

    ABPAREN = r'\('
    CEPAREN = r'\)'
    ABLLAVE = r'\{'
    CELLAVE = r'\}'
    COMA = r','
    PUNTOYCOMA = r';'

    NUMBER = r'number'
    STRING = r'string'
    BOOLEAN = r'boolean'
    LET = r'let'
    ALERT = r'alert'
    INPUT = r'input'
    FUNCTION = r'function'
    RETURN = r'return'
    IF = r'if'
    FOR = r'for'

    ID = r'[a-zA-Z][a-zA-Z0-9_]*'

    # ID['number'] = NUMBER
    # ID['string'] = STRING
    # ID['boolean'] = BOOLEAN
    # ID['let'] = LET
    # ID['alert'] = ALERT
    # ID['input'] = INPUT
    # ID['function'] = FUNCTION
    # ID['return'] = RETURN
    # ID['if'] = IF
    # ID['for'] = FOR

    def empty(self, t):
        t.value = ''
        return t

    def OPESP(self, t):
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

    def NUMBER(self, t):
        return self.empty(t)

    def STRING(self, t):
        return self.empty(t)

    def BOOLEAN(self, t):
        return self.empty(t)

    def LET(self, t):
        return self.empty(t)

    def ALERT(self, t):
        return self.empty(t)

    def INPUT(self, t):
        return self.empty(t)

    def FUNCTION(self, t):
        return self.empty(t)

    def RETURN(self, t):
        return self.empty(t)

    def IF(self, t):
        return self.empty(t)

    def FOR(self, t):
        return self.empty(t)

    def CTEENTERA(self, t):
        """ If the number found is bigger than 32767 calls self.error.

        Casts the token values from str to int.

        Args:
            t(Token): The integer constant token.

        Returns:
            Token: The token modified.
        """

        t.value = int(t.value)
        if t.value > 32767:
            self.error(t, "CTEENTERA")
        return t

    def CADENA(self, t):
        """If the string length is bigger than 64 calls self.error.

        Args:
            t(Token): The string constant token.

        Returns:
            Token: the same token.
        """
        if len(t.value) > 64:
            self.error(t, "CADENA")
        return t

    def CTELOGICA(self, t):
        """Modifies the argument token changing its str value to an integer value.

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

    def ID(self, t):
        tables.add(id0, t.value)
        t.value = tables.getPos(id0, t.value)
        return t

    def OPARIT(self, t):
        """Modifies the argument token changing its str value to an integer value.

        The token value is set 0 if "+" is found or 1 if "-"

        Args:
            t(Token): The token which matches an arithmetic operation.

        Returns:
            Token: The return token modified.
        """
        if t.value == '+':
            t.value = 0
        else:
            t.value = 1
        return t

    @_('\n+',
       r'(?s:/\*.*?\*/)')
    def newline(self, t):
        """Increases the line number.

        Increases the line number where the lexer is working to provide a correct information when an error is found.

        Args:
            t(Token): The token which contains a comment or a newline.
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

    def error(self, t, type_error="default"):
        """Handles lexer errors.

        An error is reported when a wrong character is found.
        Prints a description of the error and provides the number of the line and the column where it has been found.
        **Particular errors**:
            1. Value of a token which type is "CADENA" has a length greater than 64
            2. Value of a token which type is "CTE_ENTERA" is bigger than 32767

        Args:
            t(Token): The only parameter.
        """

        res = 'Error lexico: \n\t'
        if type_error == "CADENA":
            res += f'Cadena demasiado larga: "{t.value}", con logitud mayor que 64: {len(t.value)},'
        elif type_error == "CTEENTERA":
            res += f'Número fuera de rango: "{t.value},"'
        else:
            res += f'Caracter ilegal "{t.value[0]}"'
        print(f'{res} en la linea {self.lineno} y columna {self.find_column(t)}', file=sys.stderr)
        exit()

    def get_token(self):
        """Generator that yields tokens of the data text one by one.

        Finally, gives a different token which represents the end of file.

        Yields:
            Token: The next token until EOF.
        """
        for tok in self.tokenize(self.data):
            yield tok

        tok_EOF = Token()
        tok_EOF.type = 'EOF'
        tok_EOF.value = ''
        yield tok_EOF


# TS:

if __name__ == '__main__':
    # tables = SymTable()  # Creación de la instancia para el manejador de tablas
    # id0 = tables.newTable()  # Creación de la tabla global (id_ = 0)
    # id1 = tables.newTable()  # Creación de la tabla local (id_ = 1)
    # tables.add(id0, "hola")  # Añadimos en la tabla global el lex string con desplazamiento 0
    # tables.addAttribute(id0, "hola", "desplazamiento", 0)
    # lex = "number"  # {"tipo":"number", "desp":0}  # Se define number con desplazamiento 8
    # pos = tables.add(id0, lex)  # Se añade en la tabla global lex
    # print(pos)  # Imprime posición de escritura
    # quizaFalse = tables.add(id0, lex)  # Se intenta añadir otra vez lex
    # print(quizaFalse)
    # pos = tables.getPos(id0, "string")  # Buscamos posición del lex insertado en la línea 174
    # e = tables.removeLexAt(id0, pos)  # Eliminamos el lex en la posición encontrada previamente
    # print(e)  # Imprimimos el lex eliminado
    # print(tables.getPos(id0,
    #                     "hola"))  # Intentamos buscar el lex eliminado previamente y mostramos por stdout su resultado

    f = open('prueba.txt', 'r')
    data = f.read()
    tables = SymTable()
    id0 = tables.newTable()
    sys.stdout = open("Tokens.txt", "w")
    sys.stderr = open("Error.txt", "w")
    lexer = JSLexer(data)

    for tok in lexer.get_token():
        print(f'<{tok.type} , {tok.value}>')
