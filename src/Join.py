from Rel import *

class Join:
    """ Represent a JOIN request (SPJRUD)

    Attributes:
        first_relation     the first relation on which perform the request
        second_relation    the second relation on which perform the request
    """

    def __init__(self, first_relation, second_relation):
        self.initial_first_relation = first_relation
        self.first_relation = first_relation.request_relation

        self.initial_second_relation = second_relation
        self.second_relation = second_relation.request_relation

        # Perform the request
        self.request_relation = self.perform()

    def perform(self):
        """ Perform the join request to get the new relation """
        new_schema = self.first_relation.database_schema.copy()

        for attribute in self.second_relation.database_schema:
            if not attribute in new_schema:
                new_schema[attribute] = self.second_relation.database_schema[attribute]

        return Rel(self.first_relation.name + "_" + self.second_relation.name, new_schema)

    def __str__(self):
        """ Transform the request into a string """
        return f"Join({self.initial_first_relation}, {self.initial_second_relation})"