from system.SqlLiteDatabase import *

class Rel:
    """ This class represents a relation 

    Attributes:
        name                name of the relation
        database_schema     schema of the relation (Ex : {'name':TEXT, 'population':NUMERIC})
        is_final_relation   always True in case of the initial relation (not if queries)
    """

    def __init__(self, name, database_schema = {}, is_final_relation = True):
        self.checkRequest()
        self.name = name
        self.is_final_relation = is_final_relation

        self.database = SqlLiteDatabase('database.db', name)

        # Get the schema in a python dict or by the sql database
        if database_schema:
            # self.database.checkDatabase(database_schema)
            self.database_schema = database_schema
        else:
            self.database_schema = self.perform()


    def perform(self):
        """ Get the database schema in the database """ 
        return self.database.getSchema()

    def checkRequest(self):
        """ Check some conditions so that the request is valid """
        pass

    def execute(self, is_last_query = True):
        """ Execute the request """
        return self.name

    def editTableExecute(self, is_last_query, has_two_relation=False):
        """ Remove the previous request table. 

            If this is the last request ([is_last_query == True]), delete the current request table. 
            If the request take two relations (join, union, ...), the attribute [has_two_relation] is set to True 
        """

        if has_two_relation:
            # Delete the previous table but not if it's the original relation
            if not self.first_relation.is_final_relation:
                self.database.dropTable(self.first_relation.name)
            if not self.second_relation.is_final_relation:
                self.database.dropTable(self.second_relation.name)
        else:
            # Delete the previous table but not if it's the original relation
            if not self.relation.is_final_relation:
                self.database.dropTable(self.relation.name)

        # Get result table and delete the last table but only if it's the last recursive query
        if is_last_query:
            result = self.database.showTable(self.name)

            self.database.dropTable(self.name)
            return result
        
        return self.name

    def __str__(self):
        """ Transform the request into a string """
        return f"Rel({self.name})"