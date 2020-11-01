from pyTable.Table import Table


class SymTable:
    """Represents a handler of symbol tables.

    Attributes:
        tables (list of Table): Contains the different tables.
        nextId (int): The next number which a new table will take to identify itself.

    """

    def __init__(self):
        self.tables = []
        self.nextId = 0

    def existTable(self, id_):
        """Checks if the table symbol identified by an id_ exists.

        Args:
            id_ (int): The identifier of the symbol table.

        Returns:
            bool: True if it exists, False otherwise.
        """
        a = self.tables[id_]
        if not a or not a.exist():
            return False
        else:
            return True

    def destroyTable(self, id_):
        """Destroys a symbol table identified by an id_.

        Args:
            id_ (int): The identifier of the symbol table.
        """
        self.tables[id_].delete()

    def existsEntry(self, id_, lex):
        """Checks if lex is in the table identified by an id_.

        Args:
            id_ (int): Identifier of the symbol table.
            lex (str): The lexem to find into the symbol table.

        Returns:
            bool: True if lex exists, False otherwise.
        """
        return self.tables[id_].contains(lex)

    def newTable(self):
        """Creates a new symbol table.

        Returns:
            nextId: The identifier of the new symbol table.
        """

        self.tables.append(Table(self.nextId))
        self.nextId += 1
        return self.nextId - 1

    def getPos(self, id_, lex):
        """Gets the position where a lexeme is located into the symbol table identified by an id_.

        Args:
            id_ (int): Identifier of the symbol table.
            lex (str): The lexeme to find into the symbol table

        Returns:
           int or None: the position where lex is located into the symbol table if the lexeme
                is in the table, None otherwise.
        """
        return self.tables[id_].getPos(lex)

    def add(self, id_, lex):
        """Adds a lexeme into the symbol table identified by an id_.

        Args:
            id_ (int): The identifier of the symbol table.
            lex (str): The lexeme to add in the symbol table.

        Returns:
            int or None: int pos in table if the lexeme has been added, None if lex is already on the table.
        """
        return self.tables[id_].addLex(lex)

    def removeLexAt(self, idTable, posLex):
        """Removes a lexeme in a given position from the table identified by an id_.

        Args:
            idTable (int): Represents the identifying of the symbol table.
            posLex (int): The position that is going to be removed.

        Returns:
            dict or None: dict the lexeme deleted, None if index is out of bounds.
        """
        return self.tables[idTable].removeLexAt(posLex)

    def addAttribute(self, id_, lex, type_, content):
        """Adds an attribute to a lexeme in the table identified by an id_.

        Args:
            id_ (int): Identifier of the symbol table.
            lex (str):  The lexeme to find into the symbol table.
            type_ (str): The type of attribute to set.
            content (any): The value of the attribute.

        Returns:
            bool: True if the attribute has been added, false otherwise(lex does not exist an the table).
        """
        return self.tables[id_].addAttribute(lex, type_, content)

    def getAttribute(self, id_, lex, type_):
        """Gets value of an attribute of a lexeme in the table identified by an id_.

        Args:
            id_ (int): Identifier of the symbol table.
            lex (str): The lexem to find into the symbol table
            type_ (str): The type of the attribute.

        Returns:
             any or None: any the value of the attribute, False if the type of the attribute does not exists.
        """
        return self.tables[id_].getAttribute(lex, type_)

    def getLexDict(self, idTable, lex):
        """Gets the dict of a specified lexeme contained in the symbol table identified by an id_.

         Returns:
            dict or None: dict dictionary of lexeme lex, None if lex is not in the symbol table.
        """
        return self.tables[idTable].getLexDict(lex)

    def getLexEntry(self, idTable, posLex):
        """Gets lexem entry is located in a given position.

        Args:
            idTable (int): Represents the identifying of the symbol table.
            posLex (int): The position into the table

        Returns:
            dict or None: dict attributes of a lexeme located into the given position, None if index is out of bounds.
        """

        return self.tables[idTable].getLexEntry(posLex)

    def writeTable(self, path):
        """Prints the content of all the tables into a file pointed by path.
            Prints the table using this format:
                CONTENIDO DE LA TABLA # 0 :

                *	LEXEMA : 'a'
                    ATRIBUTOS :
                    + DESPLAZAMIENTO : '0'
                ---------------- ----------------
                *	LEXEMA : 'a_1'
                    ATRIBUTOS :
                    + DESPLAZAMIENTO : '1'
                ---------------- ----------------
                *	LEXEMA : 'b'
                    ATRIBUTOS :
                    + DESPLAZAMIENTO : '2'
                ---------------- ----------------
                Prints one table after another
        Args:
            path (str): the path of the file.

        Returns:
            bool: True if the table exists. False otherwise.
        """
        for tab in self.tables:
            tab.write(path)
        return True
