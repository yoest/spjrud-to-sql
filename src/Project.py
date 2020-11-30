from Rel import *

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
        super().__init__(self.relation.name, self.perform())

    def perform(self):
        """ Perform the project request to get the schema """
        new_schema = {}

        # Select only some attributes in the database schema of the initial relation
        for attribute in self.relation.database_schema:
            if attribute in self.list_attributes:
                new_schema[attribute] = self.relation.database_schema[attribute]

        return new_schema

    def checkRequest(self):
        """ all attributes to compared has to be in the relation """
        for attribute in self.list_attributes:
            if not attribute in self.relation.database_schema:
                error_request = f"\n\nInvalid expression.\nThe (sub-)expression\n\t{self}\nis invalid because the schema of\n\t{self.relation}\nwhich is\n\t{self.relation.database_schema}\nhas no attribute :\n\t'{attribute}'"

                raise ValueError(error_request)

    def execute(self):
        """ Execute the request """
        request = "SELECT "

        for x, attribute in enumerate(self.list_attributes):
            request += attribute

            if(not (x == len(self.list_attributes) - 1)):
                request += ", "

        request += " FROM (" + self.relation.execute() + ")"
        return request

    def __str__(self):
        """ Transform the request into a string """
        return f"Project({self.list_attributes}, {self.relation})"