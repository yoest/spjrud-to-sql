from spjrud_converter.relations.Rel import *

class Project(Rel):
    """ Represent a PROJECT request (SPJRUD)

    Attributes:
        list_attributes     all the attributes to 'extract' from the relation
        relation            the relation on which perform the projection
    """

    def __init__(self, list_attributes, relation):
        self.list_attributes = list_attributes
        self.relation = relation

        # Perform the request
        super().__init__(self.relation.name + "_proj", self.perform(), False)

    def perform(self):
        """ Perform the project request to get the schema """
        new_schema = {}

        # Select only some attributes in the database schema of the initial relation
        for attribute in self.relation.database_schema:
            if attribute in self.list_attributes:
                new_schema[attribute] = self.relation.database_schema[attribute]

        return new_schema

    def check_request(self):
        """ all attributes to compared has to be in the relation """
        for attribute in self.list_attributes:
            if not attribute in self.relation.database_schema:
                error_request = f"\n\nInvalid expression.\nThe (sub-)expression\n\t{self}\nis invalid because the schema of\n\t{self.relation}\nwhich is\n\t{self.relation.database_schema}\nhas no attribute :\n\t'{attribute}'"

                raise ValueError(error_request)

    def execute(self, is_last_query = True):
        """ Execute the request """
        request = "SELECT DISTINCT "

        # Formating list of attriutes to get "name of attribute 1, name of attribute 2, ..."
        for x, attribute in enumerate(self.list_attributes):
            request += attribute

            # Add a comma only if it's not the end of the list
            if not (x == len(self.list_attributes) - 1):
                request += ", "

        request += " FROM (" + self.relation.execute(False) + ")"

        # Create the table in the database
        self.database.execute_request(self.name, request)
        
        return super().edit_table_execute(is_last_query)

    def __str__(self):
        """ Transform the request into a string """
        return f"Project({self.list_attributes}, {self.relation})"