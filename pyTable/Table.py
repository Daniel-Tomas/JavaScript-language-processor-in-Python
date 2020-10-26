"""
Software distributed under a Creative Commons Attribution-ShareAlike 3.0 Unported license. This allows you to adapt, copy, distribute and transmit the work while crediting the author of the original work and sharing under the same or similar license.
Full legal text of this license can be found on http://creativecommons.org/licenses/by-sa/3.0/legalcode
"""


class Table:
    """The class which makes an instance of a symbol table.

    Attributes:
        lexems (list): A list which represents lexems in the table.
        exists (bool): Represents if the table exists or not.
        id_ (int): Represents the identifying of the table.
    """

    def __init__(self, id_):
        self.lexems = []
        self.exists = True
        self.id = id_

    def delete(self):
        """Function to mark the table as deleted.
        """
        self.exists = False

    def exist(self):
        """Function which checks wether the table symbol exists or not.

        Returns:
            bool: True if it exists, False otherwise.
        """
        return self.exists

    def addLex(self, lex):
        """Function used to add the lexem lex into the symbol table identify by id.

        Args:
            lex (str): The lexem to add in the symbol table.

        Returns:
            int or bool: int pos in table if everything was Ok, false if lex is already on the table.
        """
        for element in self.lexems:
            if element["lex"] == lex:
                return False
        self.lexems.append({"lex": lex})
        return len(self.lexems) - 1

    def addAttribute(self, lex, type_, content):
        """Function adds a characteristic to the lexem.

        Args:
            lex (str): The lexem to find into the symbol table.
            type_ (str): The type to set.
            content (any): The value of the type

        Returns:
            bool: True if everything is OK, false otherwise(lex does not exist an the table).
        """
        lexDict = self.getLexDict(lex)
        if not lexDict:
            return False
        lexDict[type_] = content
        return True

    def getLexDict(self, lex):
        """Function to get the dict of a specified lex"""
        for e in self.lexems:
            if e["lex"] == lex:
                return e
        return False

    def getLexEntry(self, posLex):
        """Gets the lexem which is located in a given position.

        Args:
            posLex (int): The position into the table

        Returns:
            str or bool: str lexem located into the given position, false otherwise(lex does not exist an the table).
        """

        if posLex >= len(self.lexems):
            return False

        return self.lexems[posLex]

    def removeLexAt(self, posLex):
        """Function to remove a lexem in a given position from the table.

        Args:
            posLex (int): The position that is going to be removed.

        Returns:
            dict: the lexem deleted.
        """
        if posLex >= len(self.lexems):
            return False

        return self.lexems.pop(posLex)

    def getAttribute(self, lex, feature):
        """Gets features of a lexeme.

        Args:
            lex (str): The lexeme to find into the symbol table

        Returns:
            str: the type of a lexeme given.
        """

        lexDict = self.lexems[self.getPos(lex)]
        return lexDict.get(feature)

    def contains(self, lex):
        """Checks if lex is in the table or not."

        Args:
            lex (str): The lexeme to find into the symbol table

        Returns:
            bool: True if lex exists, False otherwise.
        """

        return True if self.getPos(lex) else False

    def write(self, path):
        """Prints the content of the table into a file pointed by path.

        Args:
            path (str): the path of the file.

        Returns:
            bool: True if the table exists. False otherwise.
        """

        if not self.exist():
            return False

        to_write = f'--------------------| Tabla {str(self.id)} |--------------------\n'
        to_write += '----------------------------------------------------\n'
        for dict_ in self.lexems:
            to_write += f'\t{str(dict_)}'
            if self.lexems[dict_] != '':
                to_write += f' ({self.lexems[dict_]})'
            to_write += '\n'
        to_write += '\n\n\n'

        with open(path, 'a') as f:
            f.write(to_write)
        return True

    def getPos(self, lex):
        """Gets the lex position in symbol table.

        Args:
            lex (str): The lexem to find into the symbol table.

        Returns:
            bool or int: the position where lex is located into the symbol table if the lexeme
            is in the table, False otherwise.
        """

        for index, dict_ in enumerate(self.lexems):
            if dict_["lex"] == lex:
                return index

        return False
