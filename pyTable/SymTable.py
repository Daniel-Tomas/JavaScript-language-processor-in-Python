from . Table import Table


class SymTable:
    """Represents a handler of symbol tables.

    Attributes:
        tables (list of Table): Contains the different tables.
        nextId (int): The next number which a new table will take to identify itself.

    """

    def __init__(self):
        self.tables = []
        self.nextId = 0

    def exist_table(self, id_):
        """Checks if the table symbol identified by an id_ exists.

        Args:
            id_ (int): The identifier of the symbol table.

        Returns:
            bool: True if it exists, False otherwise.
        """
        a = self.tables[id_]
        return a and a.exist()

    def destroy_table(self, id_):
        """Destroys a symbol table identified by an id_.

        Args:
            id_ (int): The identifier of the symbol table.
        """
        self.tables[id_].delete()

    def exists_entry(self, id_, lex):
        """Checks if lex is in the table identified by an id_.

        Args:
            id_ (int): Identifier of the symbol table.
            lex (str): The lexem to find into the symbol table.

        Returns:
            bool: True if lex exists, False otherwise.
        """
        return self.tables[id_].contains_lex(lex)

    def new_table(self):
        """Creates a new symbol table.

        Returns:
            nextId: The identifier of the new symbol table.
        """

        self.tables.append(Table(self.nextId))
        self.nextId += 1
        return self.nextId - 1

    def get_pos(self, id_, lex):
        """Gets the position where the table identified by the id_ stores the lex.

        Args:
            id_ (int): Identifier of the symbol table.
            lex (str): The lexeme to find into the symbol table

        Returns:
           int or None: the position where lex is located or None otherwise
        """
        return self.tables[id_].get_pos(lex)

    def add_entry(self, id_, lex):
        """Adds a lexeme into the symbol table identified by an id_.

        Args:
            id_ (int): The identifier of the symbol table.
            lex (str): The lexeme to add_entry in the symbol table.

        Returns:
            int or None: int pos in table if the lexeme has been added, None otherwise.
        """
        return self.tables[id_].add_lex(lex)

    def remove_lex_at(self, id_table, pos_lex):
        """Removes a lexeme located in pos_lex from the table identified by an id_.

        Args:
            id_table (int): Represents the identifying of the symbol table.
            pos_lex (int): The position that is going to be removed.

        Returns:
            dict or None: dict is the lexeme deleted, None if index is out of bounds.
        """
        return self.tables[id_table].remove_lex_at(pos_lex)

    def add_attribute(self, id_, lex, type_, content):
        """Adds an attribute to a lexeme in the table identified by id_.

        Args:
            id_ (int): Identifier of the symbol table.
            lex (str):  The lexeme to find into the symbol table.
            type_ (str): The type of attribute to set.
            content (any): The value of the attribute.

        Returns:
            bool: True if the attribute has been added, false otherwise.
        """
        return self.tables[id_].add_attribute(lex, type_, content)

    def get_attribute(self, id_, lex, type_):
        """Gets value of an attribute of a lexeme in the table identified by id_.

        Args:
            id_ (int): Identifier of the symbol table.
            lex (str): The lexem to find into the symbol table
            type_ (str): The type of the attribute.

        Returns:
             any or None: any the value of the type_, False if the type does not exist.
        """
        return self.tables[id_].get_attribute(lex, type_)

    def get_lex_dict(self, id_table, lex):
        """Gets the dict of a specified lexeme stored in the table identified by id_.

         Returns:
            dict or None: dict dictionary of lex, None if lex isn't located in table.
        """
        return self.tables[id_table].get_lex_dict(lex)

    def get_lex_entry(self, id_table, pos_lex):
        """Gets lexem entry is located in a given position.

        Args:
            id_table (int): Represents the identifying of the symbol table.
            pos_lex (int): The position into the table

        Returns:
            dict or None: dict lexeme located at pos_lex, None if otherwise
        """

        return self.tables[id_table].get_lex_entry(pos_lex)

    def write_table(self, path):
        """Prints the content of all the tables into a file pointed by
         path.
            Prints the table using the format in FormatoImpresiónTablaDeSímbolos.txt
        Args:
            path (str): the path of the file.

        Returns:
            bool: True if the table exists. False otherwise.
        """
        for tab in self.tables:
            tab.write(path)
        return True
