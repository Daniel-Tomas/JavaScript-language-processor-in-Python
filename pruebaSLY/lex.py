from sly import Lexer


class JSLexer(Lexer):

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

    ABPAREN = r'[(]'
    CEPAREN = r'[)]'
    ABLLAVE = r'[{]'
    CELLAVE = r'[}]'
    COMA = r'[,]'
    PUNTOYCOMA = r'[;]'
    # EOF = '\Z'

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

    # Revisar EOF quizá lo hace automáticamente
    literals = {'{', '}', ',', ';', '/d'}

    def CTEENTERA(self, t):
        """Function called when a token which belongs to an integer constant is found.

        Args:
            t(token): The only parameter.

        Returns:
            token: The return value. It's modified to change de value to an Integer value.

        Raises:
            IOError: If value is bigger than the maximum integer allowed.
        """

        t.value = int(t.value)
        if t.value > 32767:
            self.error(t, "CTE_ENTERA")
        return t

    def CADENA(self, t):
        """Function called when a token which belongs to an string constant is found.

            Args:
                t(token): The only parameter.

            Returns:
                token: The return value which is modified to delete the quotation marks.

            Raises:
                IOError: if the length of the string is bigger than 64.
            """
        t.value = t.value[1:-1]
        if len(t.value) > 64:
            self.error(t, "CADENA")
        return t

    def CTELOGICA(self, t):
        """Called when a token which is a logical constant is found

        It modifies the argument token changing its str value to an int value.
        The token value will be 0 if "false" is found or 1 if "true"

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

    # TODO: Para hacer cuando se de la TS
    # def ID(self,t):

    def OPARIT(self, t):
        """Function called when a token which arithmetical operator is found.

            Args:
                t(token): The only parameter.

            Returns:
                token: The return value. It's modified to change de value to an Integer value.
                This token's integer value will be 0 if "+" is found or 1 if "-"
        """
        if t.value == '+':
            t.value = 0
        else:
            t.value = 1
        return t

    @_('\n+',
       r'(?s:/\*.*?\*/)')  # re.DOTALL only for this re expression
    def newline(self, t):
        self.lineno += t.value.count('\n')

    # Compute column.
    #     input is the input text string
    #     token is a token instance
    def find_column(self, token):
        last_cr = self.text.rfind('\n', 0, token.index)
        if last_cr < 0:
            last_cr = 0
        column = (token.index - last_cr)
        return column

    def error(self, t, type_error="default"):
        """Function called when a wrong character is found.

        A character is wrong if it does not belong to a correct token in that very position.
        It prints and exit

            Args:
               t(token): The only parameter.

        """

        if type_error == "CADENA":
            res = f'Cadena demasiado larga: "{t.value}", con logitud mayor que 64: {len(t.value)},'
        elif type_error == "CTE_ENTERA":
            res = f'Número fuera de rango: "{t.value}"'
        else: # TODO: hacer cambios de idioma, para que tenga consistencia, en español el output, y en ingles todo lo demas, ¿no?
            res = f'Illegal character "{t.value[0]}"'
        print(f'{res} en la linea {self.lineno} y columna {self.find_column(t)}')
        exit()


if __name__ == '__main__':
    # data = 'x_Aa= 3 + 42 * (s - t)'
    # data = '''int a=2;
    #     a = a + 2; a_1/*a &
    #
    #     adasdas */
    #     /* asd/asd*/ true
    #     false true
    #     /*"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"*/
    #
    #     if (a ==32766 & b == 2) _
    #     a--;'''
    f = open('prueba.txt', 'r')
    data = f.read()
    lexer = JSLexer(data)
    for tok in lexer.tokenize(data):
        print(f'< {tok.type} , {tok.value} >')
