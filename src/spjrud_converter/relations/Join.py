from spjrud_converter.relations.Rel import *

class Join(Rel):
    """ Represent a JOIN request (SPJRUD)

    Attributes:
        first_relation     the first relation on which perform the request
        second_relation    the second relation on which perform the request
    """

    def __init__(self, first_relation, second_relation):
        self.first_relation = first_relation
        self.second_relation = second_relation

        # Perform the request
        super().__init__(self.first_relation.name + "_" + self.second_relation.name + "_join", self.perform(), False)

    def perform(self):
        """ Perform the join request to get the new schema """
        new_schema = self.first_relation.database_schema.copy()

        for attribute in self.second_relation.database_schema:
            if not attribute in new_schema:
                new_schema[attribute] = self.second_relation.database_schema[attribute]

        return new_schema

    def execute(self, is_last_query = True):
        """ Execute the request """
        request = "SELECT *"
        request += " FROM (" + self.first_relation.execute(False) + " NATURAL INNER JOIN " + self.second_relation.execute(False) + ")"

        self.database.executeRequest(self.name, request)

        return super().editTableExecute(is_last_query, True)

    def __str__(self):
        """ Transform the request into a string """
        return f"Join({self.first_relation}, {self.second_relation})"