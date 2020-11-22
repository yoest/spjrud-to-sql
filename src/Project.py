from Rel import *

class Project:
    """ Represent a PROJECT request (SPJRUD)

    Attributes:
        list_attributes     all the attributes to 'extract' from the relation
        relation            the relation on which perform the projection
    """

    def __init__(self, list_attributes, relation):
        self.list_attributes = list_attributes
        self.relation = relation

        # The attribute to compared has to be in the relation
        for attribute in list_attributes:
            if not attribute in relation.database_schema:
                raise Exception("Attribut is not in the relation")

    def perform(self):
        """ Perform the project request to get the relation """
        new_schema = {}

        # Select only some attributes in the database schema of the initial relation
        for attribute in self.relation.database_schema:
            if attribute in self.list_attributes:
                new_schema[attribute] = self.relation.database_schema[attribute]

        return Rel(self.relation.name, new_schema)