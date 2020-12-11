from spjrud_converter.relations.Rel import *

class SelectAttr(Rel):
    """ Represent a SELECT (attribute equal attribute) request (SPJRUD)

    Attributes:
        comparison  condition of selection (equality, ...)
        relation    the relation on which perform the comparison
    """

    def __init__(self, comparison, relation):
        self.comparison = comparison
        self.relation = relation

        # Perform the request
        super().__init__(self.relation.name + "_selatt", is_final_relation=False)

    def perform(self):
        """ Perform the select request to get the schema """
        return self.relation.database_schema

    def checkRequest(self):
        """ Both attributes to compared has to be in the relation """
        self.checkAttributes(self.comparison.name_attribute)
        self.checkAttributes(self.comparison.value)

        """ Attributes has to be of the same type """
        if not (self.relation.database_schema[self.comparison.name_attribute] == self.relation.database_schema[self.comparison.value]):
            error_request = f"\n\nInvalid expression.\nThe (sub-)expression\n\t{self}\nis invalid because the schema of\n\t{self.relation}\nwhich is\n\t{self.relation.database_schema}\nis not of the same type as this attribute :\n\t'{self.comparison.value}'"

            raise ValueError(error_request)

    def checkAttributes(self, specific_attribute):
        """ Check that the [specific_attribute] is in the current relation """
        if not specific_attribute in self.relation.database_schema:
            error_request = f"\n\nInvalid expression.\nThe (sub-)expression\n\t{self}\nis invalid because the schema of\n\t{self.relation}\nwhich is\n\t{self.relation.database_schema}\nhas no attribute :\n\t'{specific_attribute}'"

            raise ValueError(error_request)

    def execute(self, is_last_query = True):
        """ Execute the request """
        request = "SELECT *"
        request += " FROM (" + self.relation.execute(False) + ")"
        request += " WHERE " + self.comparison.name_attribute + self.comparison.operator + self.comparison.value

        # Create the table in the database
        self.database.executeRequest(self.name, request)

        return super().editTableExecute(is_last_query)

    def __str__(self):
        """ Transform the request into a string """
        return f"SelectAttr({self.comparison}, {self.relation})"