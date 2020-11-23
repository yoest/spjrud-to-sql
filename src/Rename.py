from Rel import *

class Rename:
    """ Represent a RENAME request (SPJRUD)

    Attributes:
        attribute   the attribute to rename
        new_name    new name to give to the attribute
        relation    the relation on which perform the request
    """

    def __init__(self, attribute, new_name, relation):
        self.attribute = attribute
        self.new_name = new_name
        self.relation = relation.request_relation

        # The attribute to compared has to be in the relation
        if not self.attribute in self.relation.database_schema:
            raise Exception("Attribut is not in the relation")

        # Perform the request
        self.request_relation = self.perform()

    def perform(self):
        """ Perform the select request to get the new relation """
        new_schema = self.relation.database_schema.copy()
        new_schema[self.new_name] = new_schema.pop(self.attribute)

        return Rel(self.relation.name, new_schema)