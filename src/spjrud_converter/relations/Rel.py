from spjrud_converter.system.SqlLiteDatabase import *

class Rel:
    """ This class represents a relation 

    Attributes:
        name                name of the relation
        database_schema     schema of the relation (Ex : {'name':TEXT, 'population':NUMERIC})
        is_final_relation   always True in case of the initial relation (not if queries)
    """

    def __init__(self, name, database_schema = {}, is_final_relation = True):
        # Check that the request is valid with this schema
        self.checkRequest()

        self.name = name
        self.is_final_relation = is_final_relation

        self.database = SqlLiteDatabase.getInstance()

        # Get the schema in a python dict or by the sql database
        if database_schema:
            self.database_schema = database_schema
        else:
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

    def editTableExecute(self, is_last_query, has_two_relation=False):
        """ Remove the previous request table. 

            If this is the last request ([is_last_query == True]), return the table
            Else, return the name of the request relation

            If the request take two relations (join, union, ...), the attribute [has_two_relation] is set to True 
        """
        # Update the schema
        self.database_schema = self.database.getSchema(self.name)

        # Delete the previous table but not if it's the original relation
        if has_two_relation:
            self.checkDropping(self.first_relation)
            self.checkDropping(self.second_relation)
        else:
            self.checkDropping(self.relation)

        # Get result table but only if it's the last recursive query
        if is_last_query:
            return self.database.getTable(self.name)
        
        return self.name

    def checkDropping(self, specific_relation):
        """ Drop a table only if this is not the original relation
            [specific_relation] is the name of the table
        """
        if not specific_relation.is_final_relation:
            self.database.dropTable(specific_relation.name)

    def __str__(self):
        """ Transform the request into a string """
        return f"Rel({self.name})"