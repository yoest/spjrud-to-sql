from Rel import *

class Union(Rel):
    """ Represent a UNION request (SPJRUD)

    Attributes:
        first_relation     the first relation on which perform the request
        second_relation    the second relation on which perform the request
    """

    def __init__(self, first_relation, second_relation):
        self.first_relation = first_relation
        self.second_relation = second_relation

        # Perform the request
        super().__init__(self.first_relation.name + "_" + self.second_relation.name, self.perform())

    def perform(self):
        """ Perform the union request to get the new schema """
        return self.first_relation.database_schema

    def checkRequest(self):
        """ Both relations has to have the same attributes """
        hasSameAttributes = True
        for attribute in self.first_relation.database_schema:
            if not attribute in self.second_relation.database_schema:
                hasSameAttributes = False

        hasSameSize = len(self.first_relation.database_schema) == len(self.second_relation.database_schema)

        if not hasSameAttributes or not hasSameSize:
            error_request = f"\n\nInvalid expression.\nThe (sub-)expression\n\t{self}\nis invalid because the schema of\n\t{self.first_relation}\nwhich is\n\t{self.first_relation.database_schema}\nis not the same as the schema of\n\t{self.second_relation}\nwhich is\n\t{self.second_relation.database_schema}"

            raise ValueError(error_request)

    def __str__(self):
        """ Transform the request into a string """
        return f"Union({self.first_relation}, {self.second_relation})"