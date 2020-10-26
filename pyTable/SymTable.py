from pyTable.Table import Table


# TODO: buscar en internet cual es el standard para sacar elemenentos de un dict, tenemos inconsistencias
# TODO: faltan poner bien comentarios y que tengan consistencia, tambien el Table.py

class SymTable:
    """The class which makes an instance of a symbol table.

    Attributes:
        tables (list): A list which represents the different tables.
        nextId (int): The next number which a new table will take to identify itself.

    """

    def __init__(self):
        self.tables = []
        self.nextId = 0

    def newTable(self):
        """Function create a new symbol table.

        Returns:
            nextId: which represents the ID of the new symbol table.
        """

        self.tables.append(Table(self.nextId))
        self.nextId += 1
        return self.nextId - 1

    def destroyTable(self, id_):
        """Function destroy a new symbol table.

        Args:
            id_ (int): Represents the identifying of the symbol table.

        Returns:
            int: which represents the ID of the new symbol table.
        """
        self.tables[id_].delete()

    def existTable(self, id_):
        """Function which checks wether the table symbol identify by id_ exists or not

        Args:
            id_ (int): Represents the identifying of the symbol table.
        Returns:
            bool: True if it exists, False otherwise.
        """
        a = self.tables[id_]
        if not a or not a.exist():
            return False
        else:
            return True

    def add(self, id_, lex):
        """Function used to add the lexem lex into the symbol table identify by id_

        Args:
            id_ (int): Represents the identifying of the symbol table.
            lex (str): The lexem to add in the symbol table.

        Returns:
            bool or str: str id_ if everything was Ok, false if lex is already on the table.
        """
        return self.tables[id_].addLex(lex)

    def getPos(self, id_, lex):
        """Function to know where the lex is located into the symbol table id_.

        Args:
            id_ (int): Represents the identifying of the symbol table.
            lex (str): The lexem to find into the symbol table

        Returns:
            int: the position where the lexem is located into the symbol table.
        """
        return self.tables[id_].getPos(lex)

    def getLexDict(self, idTable, lex):
        """Function to get the dict of a specified lex"""
        return self.tables[idTable].getLexDict(lex)

    def getLexEntry(self, idTable, posLex):
        """Function to know what lexem entry is located in a given position.

        Args:
            idTable (int): Represents the identifying of the symbol table.
            posLex (int): The position into the table

        Returns:
            dict: the lexem located in the given table and in the given position.
        """
        return self.tables[idTable].getLexEntry(posLex)

    def removeLexAt(self, idTable, posLex):
        """Function remove a lexem in a given position from a table.

        Args:
            idTable (int): Represents the identifying of the symbol table.
            posLex (int): The position that is going to be removed.

        Returns:
            str: the lexem deleted.
        """
        return self.tables[idTable].removeLexAt(posLex)

    def addAttribute(self, id_, lex, type_, content):
        """Function adds a characteristic to the lexem.

        Args:
            id_ (int): Represents the identifying of the symbol table.
            lex (str): The lexem to find into the symbol table.
            type_ (str): The type to set.
            content (any): The content of the type

        Returns:
            bool: True if everithing is OK, false otherwise(lex does not exist an the table).
        """
        return self.tables[id_].addAttribute(lex, type_, content)

    def getAttribute(self, id_, lex, characteristic):
        """Function to know the characteristic of a lexem.

        Args:
            id_ (int): Represents the identifying of the symbol table.
            lex (str): The lexem to find into the symbol table
            characteristic (str): The lexem to find into the symbol table

        Returns:
            str: the characteristic of a lexem given.
        """
        return self.tables[id_].getAttribute(lex, characteristic)

    def existsEntry(self, id_, lex):
        """Function destroy a new symbol table.

        Args:
            id_ (int): Represents the identifying of the symbol table.
            lex (str): The lexem to find into the symbol table

        Returns:
            bool: True if lex exists, False otherwise.
        """
        return self.tables[id_].contains(lex)

    def writeTable(self, path):
        """Prints the content of all the tables into a file pointed by path.

        Args:
            path (str): the path of the file.

        Returns:
            bool: True always.
        """

        for tab in self.tables:
            tab.write(path)
        return True
