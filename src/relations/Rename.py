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
        super().__init__(self.relation.name + "_ren", is_final_relation=False)

    def perform(self):
        """ Perform the rename request to get the new schema """
        new_schema = self.relation.database_schema.copy()
        new_schema[self.new_name] = new_schema.pop(self.attribute)

        return new_schema

    def checkRequest(self):
        """ The attribute to compared has to be in the relation and that there 
            is not another attributes with this name 
        """
        if not self.attribute in self.relation.database_schema:
            error_request = f"\n\nInvalid expression.\nThe (sub-)expression\n\t{self}\nis invalid because the schema of\n\t{self.relation}\nwhich is\n\t{self.relation.database_schema}\nhas no attribute :\n\t'{self.attribute}'"

            raise ValueError(error_request)

        if self.new_name in self.relation.database_schema:
            error_request = f"\n\nInvalid expression.\nThe (sub-)expression\n\t{self}\nis invalid because the schema of\n\t{self.relation}\nwhich is\n\t{self.relation.database_schema}\nhas already an attribute named :\n\t'{self.new_name}'"

            raise ValueError(error_request)

    def execute(self, is_last_query = True):
        """ Execute the request """
        self.relation.execute(False)

        request = "ALTER TABLE " + self.name
        request += " RENAME COLUMN " +  self.attribute
        request += " TO " +  self.new_name

        self.database.executeRequest(self.name, request, self.relation.name)

        print(self.database.getSchema())
        
        return super().editTableExecute(is_last_query)

    def __str__(self):
        """ Transform the request into a string """
        return f"Rename('{self.attribute}', '{self.new_name}', {self.relation})"