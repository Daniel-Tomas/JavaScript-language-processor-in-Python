from sly import Lexer


class CalcLexer(Lexer):
    tokens = {CTE_ENTERA, CADENA, CTE_LOGICA, OP_ARIT, OP_ESP,
              OP_REL, OP_LOG, OP_ASIG, ID, NUMBER, STRING, BOOLEAN, LET, ALERT,
              INPUT, FUNCTION, RETURN, IF, FOR, EOF}

    ignore = r' \t\n'

    # Tokens
    CTE_ENTERA = r'\d+'
    CADENA = r'".*?"'
    CTE_LOGICA = r'true|false'
    OP_ESP = r'--'
    OP_ARIT = r'\+|-'
    OP_REL = r'=='
    OP_ASIG = r'='
    OP_LOG = r'&&'

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
    literals = {'(', ')', '{', '}', ',', ';', '/d'}

    def CTE_ENTERA(self, t):
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
            print(f'Número fuera de rango: "{t.value}"')
            exit()
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
            print(f'Cadena demasiado larga: "{t.value, len(t.value)}"')
            exit()
        return t

    # TODO: Para hacer cuando se de la TS
    # def ID(self,t):

    def OP_ARIT(self, t):
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

    @_(r'\n+',
       r'(?s:/\*.*?\*/)')  # re.DOTALL only for this re expression
    def newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        """Function called when a wrong character is found.

        A character is wrong if it does not belong to a correct token in that very position.
        It prints and exit

            Args:
               t(token): The only parameter.

        """
        print(f'Illegal character "{t.value[0]}" in line {self.lineno}')
        exit()


if __name__ == '__main__':
    # data = 'x_Aa= 3 + 42 * (s - t)'
    data = '''int a=2; 
    a = a + 2; a_1/*a 
    
    adasdas */ 
    /* asd/asd*/ true
    false true
    if (a ==1 & b == 2) _
    a--;'''
    lexer = CalcLexer()
    for tok in lexer.tokenize(data):
        print(f'< {tok.type} , {tok.value} >')
