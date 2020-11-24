from Rel import *

class Union:
    """ Represent a UNION request (SPJRUD)

    Attributes:
        first_relation     the first relation on which perform the request
        second_relation    the second relation on which perform the request
    """

    def __init__(self, first_relation, second_relation):
        self.initial_first_relation = first_relation
        self.first_relation = first_relation.request_relation

        self.initial_second_relation = second_relation
        self.second_relation = second_relation.request_relation

        # Both relations has to have the same attributes
        hasSameAttributes = True
        for attribute in self.first_relation.database_schema:
            if not attribute in self.second_relation.database_schema:
                hasSameAttributes = False

        hasSameSize = len(self.first_relation.database_schema) == len(self.second_relation.database_schema)

        if not hasSameAttributes or not hasSameSize:
            raise Exception("The two relations haven't the exact same attributs")

        # Perform the request
        self.request_relation = self.perform()

    def perform(self):
        """ Perform the union request to get the new relation """
        return Rel(self.first_relation.name + "_" + self.second_relation.name, self.first_relation.database_schema)

    def __str__(self):
        """ Transform the request into a string """
        return f"Union({self.initial_first_relation}, {self.initial_second_relation})"