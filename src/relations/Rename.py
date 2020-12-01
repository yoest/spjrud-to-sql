from relations.Rel import *

class Rename(Rel):
    """ Represent a RENAME request (SPJRUD)

    Attributes:
        attribute   the attribute to rename
        new_name    new name to give to the attribute
        relation    the relation on which perform the request
    """

    def __init__(self, attribute, new_name, relation):
        self.attribute = attribute
        self.new_name = new_name

        self.relation = relation
        
        # Perform the request
        super().__init__(self.relation.name)

    def perform(self):
        """ Perform the rename request to get the new schema """
        new_schema = self.relation.database_schema.copy()
        new_schema[self.new_name] = new_schema.pop(self.attribute)

        return new_schema

    def checkRequest(self):
        """ The attribute to compared has to be in the relation """
        if not self.attribute in self.relation.database_schema:
            error_request = f"\n\nInvalid expression.\nThe (sub-)expression\n\t{self}\nis invalid because the schema of\n\t{self.relation}\nwhich is\n\t{self.relation.database_schema}\nhas no attribute :\n\t'{self.attribute}'"

            raise ValueError(error_request)

    def __str__(self):
        """ Transform the request into a string """
        return f"Rename('{self.attribute}', '{self.new_name}', {self.relation})"