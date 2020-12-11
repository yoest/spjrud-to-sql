class Displayer:
    """ Display all informations about a table

    Attributes:
        database_schema     schema of the table to display
        table               all column about the table
    """
    def __init__(self, database_schema, table):
        self.database_schema = database_schema
        self.table = table

    def show(self):
        """ Show the table to the terminal """
        result = "| "

        # Attributes
        for attribute in self.database_schema:
            result += ("%20s" % attribute) + " | "

        print(result)
        print('-' * (len(result) - 1))

        # Value of each attribute
        for row in self.table:
            result = "| "
            for column in row:
                result += ("%20s" % str(column)) + " | "

            print(result)
            print('-' * (len(result) - 1))
