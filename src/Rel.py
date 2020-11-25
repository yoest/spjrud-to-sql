class Rel:
    """ This class represents a relation 

    Attributes:
        name                name of the relation
        database_schema     schema of the relation (Ex : {'name':TEXT, 'population':NUMERIC})
    """

    def __init__(self, name, database_schema = {}):
        self.checkRequest()

        # Get the schema in a python dict or by the sql database (--TO-DO--)
        if not database_schema:
            self.database_schema = self.perform()
        else:
            self.database_schema = database_schema

        self.name = name

    def perform(self):
        """ Get the initial database schema """
        return self.database_schema

    def checkRequest(self):
        """ Check some conditions so that the request is valid """
        pass

    def __str__(self):
        """ Transform the request into a string """
        return f"Rel({self.name})"