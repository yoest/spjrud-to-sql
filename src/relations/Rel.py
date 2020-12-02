from system.SqlLiteDatabase import *

class Rel:
    """ This class represents a relation 

    Attributes:
        name                name of the relation
        database_schema     schema of the relation (Ex : {'name':TEXT, 'population':NUMERIC})
    """

    def __init__(self, name, database_schema = {}):
        self.checkRequest()
        self.name = name

        self.database = SqlLiteDatabase('database.db', name)

        # Get the schema in a python dict or by the sql database (--TO-DO--)
        if database_schema:
            self.database_schema = self.database.createTable(database_schema)

        self.database_schema = self.perform()


    def perform(self):
        """ Get the database schema in the database """ 
        return self.database.getSchema(self.name)

    def checkRequest(self):
        """ Check some conditions so that the request is valid """
        pass

    def execute(self, is_last_query = True):
        """ Execute the request """
        return self.name

    def __str__(self):
        """ Transform the request into a string """
        return f"Rel({self.name})"