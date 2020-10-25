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
        self.lexems = {}
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

    def add(self, lex):
        """Function used to add the lexem lex into the symbol table identify by id

        Args:
            lex (str): The lexem to add in the symbol table.

        Returns:
            bool or str: str lexem if everithing was Ok, false if lex is already on the table.
        """
        if not lex in self.lexems:
            self.lexems[lex] = ''
            return self.getPos(lex)
        else:
            return False

    def setType(self, lex, type):
        """Function set the type of a lexem.

        Args:
            lex (str): The lexem to find into the symbol table.
            type (str): The type to set.

        Returns:
            bool: True if everithing is OK, false otherwise(lex does not exist an the table).
        """

        if lex in self.lexems:
            self.lexems[lex] = type
            return True
        else:
            return False

    def getLex(self, posLex):
        """Function to know what lexem is located in a given position.

        Args:
            posLex (int): The position into the table

        Returns:
            str: the lexem located into the given position.
        """
        i = 0
        for e in self.lexems.keys():
            if i == posLex:
                return e
            else:
                i = i + 1
        return False

    def removeLexAt(self, posLex):
        """Function to remove a lexem in a given position from the table.

        Args:
            posLex (str): The position that is going to be removed.

        Returns:
            str: the lexem deleted.
        """
        newlexems = {}
        i = 0
        removed = ()
        for e in self.lexems:
            if i != posLex:
                newlexems[e] = ''
            else:
                removed = e
            i = i + 1
        self.lexems = newlexems
        return removed

    def getType(self, lex):
        "Returns the type of lex"
        return self.lexems[lex]

    def contains(self, lex):
        "Checks if lex is in the table or not"

        return self.lexems.has_key[lex]

    def write(self, path):
        "Writes the contents of this table to the file pointed to by path"

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
        "returns the ID of lex or False if lex is not in this table"

        i = 0
        for e in self.lexems.keys():
            if e == lex:
                break
            else:
                i = i + 1
        return False if i == len(self.lexems) else i
