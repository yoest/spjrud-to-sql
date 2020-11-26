from Rel import *

class Select(Rel):
    """ Represent a SELECT request (SPJRUD)

    Attributes:
        comparison  condition of selection (equality, ...)
        relation    the relation on which perform the comparison
    """

    def __init__(self, comparison, relation):
        self.comparison = comparison
        self.relation = relation

        # Perform the request
        super().__init__(self.relation.name)

    def perform(self):
        """ Perform the select request to get the schema """
        return self.relation.database_schema

    def checkRequest(self):
        """ The attribute to compared has to be in the relation """
        if not self.comparison.name_attribute in self.relation.database_schema:
            error_request = f"\n\nInvalid expression.\nThe (sub-)expression\n\t{self}\nis invalid because the schema of\n\t{self.relation}\nwhich is\n\t{self.relation.database_schema}\nhas no attribute :\n\t'{self.comparison.name_attribute}'"

            raise ValueError(error_request)

    def __str__(self):
        """ Transform the request into a string """
        return f"Select({self.comparison}, {self.relation})"