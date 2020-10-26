"""
Software distributed under a Creative Commons Attribution-ShareAlike 3.0 Unported license. This allows you to adapt, copy, distribute and transmit the work while crediting the author of the original work and sharing under the same or similar license.
Full legal text of this license can be found on http://creativecommons.org/licenses/by-sa/3.0/legalcode
"""


class Table():
    """The class which makes an instance of a symbol table.

    Attributes:
        lexems (list): A list which represents lexems in the table.
        exist (bool): Represents if the table exists or not.
        id (int): Represents the identifying of the table.
    """

    def __init__(self, id):
        self.lexems = []
        self.exists = True
        self.id = id

    def delete(self):
        """Function to mark the table as deleted.

        Returns:
            bool: True always.
        """
        self.exists = False
        return True

    def exist(self):
        """Function which checks wether the table symbol exists or not.

        Returns:
            bool: True if it exists, False otherwise.
        """
        return self.exists

    def addLex(self, lex):
        """Function used to add the lexem lex into the symbol table identify by id

        Args:
            lex (str): The lexem to add in the symbol table.

        Returns:
            bool or int: int pos in table if everithing was Ok, false if lex is already on the table.
        """
        for element in self.lexems:
            if element["lex"] == lex:
                return False
        self.lexems.append({"lex":lex})
        return len(self.lexems)-1

    def addCharacteristic(self, lex, type, content):
        """Function adds a characteristic to the lexem.

        Args:
            lex (str): The lexem to find into the symbol table.
            type (str): The type to set.
            content (any): The value of the type

        Returns:
            bool: True if everithing is OK, false otherwise(lex does not exist an the table).
        """
        lexDict = self.getLexDict(lex)
        if not lexDict:
            return False
        lexDict[type] = content
        return True

    def getLexDict(self, lex):
        """Function to get the dict of a specified lex"""
        for e in self.lexems:
            if e["lex"] == lex:
                return e
        return False

    def getLexEntry(self, posLex):
        """Function to know what lexem is located in a given position.

        Args:
            posLex (int): The position into the table

        Returns:
            str: the lexem located into the given position.
        """
        i = 0
        for e in self.lexems:
            if i == posLex:
                return e
            else:
                i = i + 1
        return False

    def removeLexAt(self, posLex):
        """Function to remove a lexem in a given position from the table.

        Args:
            posLex (int): The position that is going to be removed.

        Returns:
            dict: the lexem deleted.
        """
        removed = self.lexems[posLex]
        del self.lexems[posLex]
        return removed

    def getCharacteristic(self, lex, characteristic):
        """Function to know the characteristic of a lexem.

        Args:
            lex (str): The lexem to find into the symbol table

        Returns:
            str: the type of a lexem given.
        """
        lexDict =  self.lexems[self.getPos(lex)]
        return lexDict.get(characteristic)

    def contains(self, lex):
        """Checks if lex is in the table or not"

        Args:
            lex (str): The lexem to find into the symbol table

        Returns:
            bool: True if lex exists, False otherwise.
        """

        return self.lexems[self.getPos(lex)]

    def write(self, path):
        """Prints the content of the table into a file pointed by path.

        Args:
            path (str): the path of the file.

        Returns:
            bool: True if the table exists. False otherwise.
        """

        if self.exist():
            f = open(path, 'a')
            f.write('--------------------| Tabla' + str(self.id) + ' |--------------------\n')
            f.write('----------------------------------------------------\n')
            for e in self.lexems.keys():
                f.write('\t' + str(e))
                if self.lexems[e] != '':
                    f.write(' (' + self.lexems[e] + ')')
                f.write('\n')
            f.write('\n\n\n')
            f.close()
            return True
        else:
            return False

    def getPos(self, lex):
        """Function to know where the lex is located into the symbol table id.

        Args:
            lex (str): The lexem to find into the symbol table.

        Returns:
            bool or int: the position where the lexem is located into the symbol table if the lexeme
            is in the table, False otherwise.
        """

        i = 0
        for e in self.lexems:
            if e["lex"] == lex:
                break
            else:
                i = i + 1
        return False if i == len(self.lexems) else i
