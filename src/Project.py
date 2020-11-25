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
                raise Exception("Attribut is not in the relation")

    def __str__(self):
        """ Transform the request into a string """
        return f"Project({self.list_attributes}, {self.relation})"