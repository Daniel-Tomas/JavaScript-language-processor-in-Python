import unittest
from pruebaSLY.lex import CalcLexer


class MyTestCase(unittest.TestCase):

    def test_cteEntera(self):
        lexer = CalcLexer()
        for tok in lexer.tokenize('23'):
            self.assertEqual("CTE_ENTERA", tok.type)
            self.assertEqual(23, tok.value)

    def test_cadena(self):
        lexer = CalcLexer()
        for tok in lexer.tokenize('"hola"'):
            self.assertEqual("CADENA", tok.type)
            self.assertEqual("hola", tok.value)

    def test_true(self):
        lexer = CalcLexer()
        for tok in lexer.tokenize('true'):
            self.assertEqual("CTE_LOGICA", tok.type)
            self.assertEqual(1, tok.value)

    def test_false(self):
        lexer = CalcLexer()
        for tok in lexer.tokenize('false'):
            self.assertEqual("CTE_LOGICA", tok.type)
            self.assertEqual(0, tok.value)

    def test_esp(self):
        lexer = CalcLexer()
        for tok in lexer.tokenize('--'):
            self.assertEqual("OP_ESP", tok.type)

    def test_add(self):
        lexer = CalcLexer()
        for tok in lexer.tokenize('+'):
            self.assertEqual("OP_ARIT", tok.type)
            self.assertEqual(0, tok.value)

    def test_minus(self):
        lexer = CalcLexer()
        for tok in lexer.tokenize('-'):
            self.assertEqual("OP_ARIT", tok.type)
            self.assertEqual(1, tok.value)

    def test_rel(self):
        lexer = CalcLexer()
        for tok in lexer.tokenize('=='):
            self.assertEqual("OP_REL", tok.type)

    def test_log(self):
        lexer = CalcLexer()
        for tok in lexer.tokenize('&&'):
            self.assertEqual("OP_LOG", tok.type)

    def test_asig(self):
        lexer = CalcLexer()
        for tok in lexer.tokenize('='):
            self.assertEqual("OP_ASIG", tok.type)

    # TODO: Implementar TS
    def test_var(self):
        lexer = CalcLexer()
        for tok in lexer.tokenize('n0mbrEVariab_e'):
            self.assertEqual("ID", tok.type)
            self.assertEqual("n0mbrEVariab_e", tok.value)  # Debe ser un puntero a la tabla de símbolos

    def test_string(self):
        lexer = CalcLexer()
        for tok in lexer.tokenize('string'):
            self.assertEqual("STRING", tok.type)

    def test_boolean(self):
        lexer = CalcLexer()
        for tok in lexer.tokenize('boolean'):
            self.assertEqual("BOOLEAN", tok.type)

    def test_let(self):
        lexer = CalcLexer()
        for tok in lexer.tokenize('let'):
            self.assertEqual("LET", tok.type)

    def test_number(self):
        lexer = CalcLexer()
        for tok in lexer.tokenize('number'):
            self.assertEqual("NUMBER", tok.type)

    def test_alert(self):
        lexer = CalcLexer()
        for tok in lexer.tokenize('alert'):
            self.assertEqual("ALERT", tok.type)

    def test_input(self):
        lexer = CalcLexer()
        for tok in lexer.tokenize('input'):
            self.assertEqual("INPUT", tok.type)

    def test_function(self):
        lexer = CalcLexer()
        for tok in lexer.tokenize('function'):
            self.assertEqual("FUNCTION", tok.type)

    def test_return(self):
        lexer = CalcLexer()
        for tok in lexer.tokenize('return'):
            self.assertEqual("RETURN", tok.type)

    def test_if(self):
        lexer = CalcLexer()
        for tok in lexer.tokenize('if'):
            self.assertEqual("IF", tok.type)

    def test_for(self):
        lexer = CalcLexer()
        for tok in lexer.tokenize('for'):
            self.assertEqual("FOR", tok.type)

    def test_openBracket(self):
        lexer = CalcLexer()
        for tok in lexer.tokenize('('):
            self.assertEqual("(", tok.type)

    def test_closeBracket(self):
        lexer = CalcLexer()
        for tok in lexer.tokenize(')'):
            self.assertEqual(")", tok.type)

    def test_openKey(self):
        lexer = CalcLexer()
        for tok in lexer.tokenize('{'):
            self.assertEqual("{", tok.type)

    def test_closeKey(self):
        lexer = CalcLexer()
        for tok in lexer.tokenize('}'):
            self.assertEqual("}", tok.type)

    def test_for(self):
        lexer = CalcLexer()
        for tok in lexer.tokenize(','):
            self.assertEqual(",", tok.type)

    def test_for(self):
        lexer = CalcLexer()
        for tok in lexer.tokenize(';'):
            self.assertEqual(";", tok.type)

    # ************************************************************************************#
    #                                                                                    #
    #                      Comienzo de las pruebas de integración                        #
    #                            #TODO: Add TS to ID part                                #
    # ************************************************************************************#

    def test_miniFunction(self):
        lexer = CalcLexer()
        data = '''function string salto ()
                    {
	                    return "\n";
                    }'''
        for indx, tok in enumerate(lexer.tokenize(data)):
            if indx == 0:
                self.assertEqual("FUNCTION", tok.type)
            elif indx == 1:
                self.assertEqual("STRING", tok.type)
            elif indx == 2:
                self.assertEqual("ID", tok.type)
            elif indx == 3:
                self.assertEqual("(", tok.type)
            elif indx == 4:
                self.assertEqual(")", tok.type)
            elif indx == 5:
                self.assertEqual("{", tok.type)
            elif indx == 6:
                self.assertEqual("RETURN", tok.type)
            elif indx == 7:
                self.assertEqual("CADENA", tok.type)
                self.assertEqual("\n", tok.value)
            elif indx == 8:
                self.assertEqual(";", tok.type)
            else:
                self.assertEqual("}", tok.type)

    def test_mediumFunction(self):
        lexer = CalcLexer()
        data = '''function number SumatorioRecursivo (number n)	/* n: parámetro formal de la función entera */
                        {
	                        if (n == 0)	return 1;
	                        /* llamada recursiva */
	                    return n + FactorialRecursivo (n - 1);
                        }
                            '''
        for indx, tok in enumerate(lexer.tokenize(data)):
            if indx == 0:
                self.assertEqual("FUNCTION", tok.type)
            elif indx == 1:
                self.assertEqual("NUMBER", tok.type)
            elif indx == 2:
                self.assertEqual("ID", tok.type)
            elif indx == 3:
                self.assertEqual("(", tok.type)
            elif indx == 4:
                self.assertEqual("NUMBER", tok.type)
            elif indx == 5:
                self.assertEqual("ID", tok.type)
            elif indx == 6:
                self.assertEqual(")", tok.type)
            elif indx == 7:
                self.assertEqual("{", tok.type)
            elif indx == 8:
                self.assertEqual("IF", tok.type)
            elif indx == 9:
                self.assertEqual("(", tok.type)
            elif indx == 10:
                self.assertEqual("ID", tok.type)
            elif indx == 11:
                self.assertEqual("OP_REL", tok.type)
            elif indx == 12:
                self.assertEqual("CTE_ENTERA", tok.type)
                self.assertEqual(0, tok.value)
            elif indx == 13:
                self.assertEqual(")", tok.type)
            elif indx == 14:
                self.assertEqual("RETURN", tok.type)
            elif indx == 15:
                self.assertEqual("CTE_ENTERA", tok.type)
                self.assertEqual(1, tok.value)
            elif indx == 16:
                self.assertEqual(";", tok.type)
            elif indx == 17:
                self.assertEqual("RETURN", tok.type)
            elif indx == 18:
                self.assertEqual("ID", tok.type)
            elif indx == 19:
                self.assertEqual("OP_ARIT", tok.type)
                self.assertEqual(0, tok.value)
            elif indx == 20:
                self.assertEqual("ID", tok.type)
            elif indx == 21:
                self.assertEqual("(", tok.type)
            elif indx == 22:
                self.assertEqual("ID", tok.type)
            elif indx == 23:
                self.assertEqual("OP_ARIT", tok.type)
                self.assertEqual(1, tok.value)
            elif indx == 24:
                self.assertEqual("CTE_ENTERA", tok.type)
                self.assertEqual(1, tok.value)
            elif indx == 25:
                self.assertEqual(")", tok.type)
            elif indx == 26:
                self.assertEqual(";", tok.type)
            else:
                self.assertEqual("}", tok.type)

    def test_mediumFunctionDev1(self):
        lexer = CalcLexer()
        data = '''function number SumatorioRecursivo(number n)	/* n: parámetro formal de la función entera */
                        {if(n==0)return 1;
	                        /* llamada recursiva ç
	                        */return n+FactorialRecursivo(n-1);}
                            '''
        for indx, tok in enumerate(lexer.tokenize(data)):
            if indx == 0:
                self.assertEqual("FUNCTION", tok.type)
            elif indx == 1:
                self.assertEqual("NUMBER", tok.type)
            elif indx == 2:
                self.assertEqual("ID", tok.type)
            elif indx == 3:
                self.assertEqual("(", tok.type)
            elif indx == 4:
                self.assertEqual("NUMBER", tok.type)
            elif indx == 5:
                self.assertEqual("ID", tok.type)
            elif indx == 6:
                self.assertEqual(")", tok.type)
            elif indx == 7:
                self.assertEqual("{", tok.type)
            elif indx == 8:
                self.assertEqual("IF", tok.type)
            elif indx == 9:
                self.assertEqual("(", tok.type)
            elif indx == 10:
                self.assertEqual("ID", tok.type)
            elif indx == 11:
                self.assertEqual("OP_REL", tok.type)
            elif indx == 12:
                self.assertEqual("CTE_ENTERA", tok.type)
                self.assertEqual(0, tok.value)
            elif indx == 13:
                self.assertEqual(")", tok.type)
            elif indx == 14:
                self.assertEqual("RETURN", tok.type)
            elif indx == 15:
                self.assertEqual("CTE_ENTERA", tok.type)
                self.assertEqual(1, tok.value)
            elif indx == 16:
                self.assertEqual(";", tok.type)
            elif indx == 17:
                self.assertEqual("RETURN", tok.type)
            elif indx == 18:
                self.assertEqual("ID", tok.type)
            elif indx == 19:
                self.assertEqual("OP_ARIT", tok.type)
                self.assertEqual(0, tok.value)
            elif indx == 20:
                self.assertEqual("ID", tok.type)
            elif indx == 21:
                self.assertEqual("(", tok.type)
            elif indx == 22:
                self.assertEqual("ID", tok.type)
            elif indx == 23:
                self.assertEqual("OP_ARIT", tok.type)
                self.assertEqual(1, tok.value)
            elif indx == 24:
                self.assertEqual("CTE_ENTERA", tok.type)
                self.assertEqual(1, tok.value)
            elif indx == 25:
                self.assertEqual(")", tok.type)
            elif indx == 26:
                self.assertEqual(";", tok.type)
            else:
                self.assertEqual("}", tok.type)

    # ************************************************************************************#
    #                                                                                    #
    #                      Comienzo de las pruebas de negación                           #
    #                                                                                    #
    # ************************************************************************************#

    def test_negateToken(self):
        lexer = CalcLexer()
        for tok in lexer.tokenize('a2a2_*'):
            self.assertEqual("ID", tok.type)
            self.assertEqual("a2a2_", tok.value)

    def test_negateToken2(self):
        lexer = CalcLexer()
        for tok in lexer.tokenize('&A&'):
            self.assertEqual("ID", tok.type)
            self.assertEqual("A", tok.value)


if __name__ == '__main__':
    lexer = CalcLexer()
    unittest.main()
