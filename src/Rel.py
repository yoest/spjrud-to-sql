class Rel:
    """ This class represents a relation 

    Attributes:
        name                name of the relation
        database_schema     schema of the relation (Ex : {'name':TEXT, 'population':NUMERIC})
    """

    def __init__(self, name, database_schema = {}):
        self.name = name
        self.database_schema = database_schema

        # Perform the request
        self.request_relation = self.perform()

    def perform(self):
        """ Get the initial database schema """
        return self