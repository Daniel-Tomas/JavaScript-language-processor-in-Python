class Table:
    """Represents a symbol table.

    Args:
        id_ (int): id to be set.

    Attributes:
        lexems (list of dict): A list which represents lexems in the table.
        exists (bool): Represents if the table exists or not.
        id_ (int): Represents the identifying of the table.

    """

    def __init__(self, id_):
        self.lexems = []
        self.exists = True
        self.id_ = id_

    def exist(self):
        """Checks if the symbol table exists.

        Returns:
            bool: True if it exists, False otherwise.
        """
        return self.exists

    def delete(self):
        """Marks the table as deleted, it will not exit."""
        self.exists = False

    def contains(self, lex):
        """Checks if lex is in the table.

        Args:
            lex (str): The lexeme to find into the symbol table.

        Returns:
            bool: True if lex exists, False otherwise.
        """

        return True if self.getPos(lex) else False

    def getPos(self, lex):
        """Gets the lexeme position in symbol table.

        Args:
            lex (str): The lexeme to find into the symbol table.

        Returns:
             int or None: the position where lex is located into the symbol table if the lexeme
                is in the table, None otherwise.
        """

        for index, dict_ in enumerate(self.lexems):
            if dict_["LEXEMA"] == lex:
                return index

        return None

    def addLex(self, lex):
        """Add a lexeme into the symbol table.

        Args:
            lex (str): The lexeme to add in the symbol table.

        Returns:
            int or None: int pos in table if the lexeme has been added, None if lex is already on the table.
        """
        for element in self.lexems:
            if element["LEXEMA"] == lex:
                return None

        self.lexems.append({"LEXEMA": lex})
        return len(self.lexems) - 1

    def removeLexAt(self, posLex):
        """Removes a lexeme in a given position from the table.

        Args:
            posLex (int): The position that is going to be removed.

        Returns:
            dict or None: dict the lexeme deleted, None if index is out of bounds.
        """
        if posLex >= len(self.lexems):
            return None

        return self.lexems.pop(posLex)

    def addAttribute(self, lex, type_, content):
        """Adds an attribute to a lexeme.

        Args:
            lex (str): The lexeme to find into the symbol table.
            type_ (str): The type of attribute to set.
            content (any): The value of the attribute.

        Returns:
            bool: True if the attribute has been added, false otherwise(lex does not exist an the table).
        """
        lexDict = self.getLexDict(lex)
        if not lexDict:
            return False

        lexDict[type_] = content
        return True

    def getAttribute(self, lex, type_):
        """Gets value of an attribute of a lexeme.

        Args:
            lex (str): The lexeme to find into the symbol table.
            type_ (str): The type of the attribute.

        Returns:
            any or None: any the value of the attribute, False if the type of the attribute does not exists.
        """

        lexDict = self.lexems[self.getPos(lex)]

        return lexDict.get(type_)

    def getLexDict(self, lex):
        """Gets the dict of a specified lexeme.

         Returns:
            dict or None: dict dictionary of lexeme lex, None if lex is not in the symbol table.
        """
        for e in self.lexems:
            if e["LEXEMA"] == lex:
                return e
        return None

    def getLexEntry(self, posLex):
        """Gets the lexeme which is located in a given position.

        Args:
            posLex (int): The position into the table

        Returns:
            dict or None: dict attributes of a lexeme located into the given position, None if index is out of bounds.
        """

        if posLex >= len(self.lexems):
            return None

        return self.lexems[posLex]

    def write(self, path):
        """Prints the content of the table into a file pointed by path.
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
        Args:
            path (str): the path of the file.

        Returns:
            bool: True if the table exists. False otherwise.
        """

        if not self.exist():
            return False

        to_write = f'CONTENIDO DE LA TABLA # {str(self.id_)} :\n'
        to_write += '\n'
        for dict_ in self.lexems:
            for i, keys in enumerate(dict_.keys()):
                if (i == 0):
                    to_write += f'*\t{keys} : \'{dict_[keys]}\''
                elif (i == 1):
                    to_write += f'\tATRIBUTOS :\n'
                    to_write += f'\t+ {keys} : \'{dict_[keys]}\''
                else:
                    to_write += f'\t+ {keys} : \'{dict_[keys]}\''
                to_write += '\n'
            to_write += f'---------------- ----------------\n'
        to_write += '\n\n\n'

        with open(path, 'a') as f:
            f.write(to_write)
        return True
