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
            # Add new attributes of the second relation
            if not attribute in new_schema:
                new_schema[attribute] = self.second_relation.database_schema[attribute]

        return new_schema

    def execute(self, is_last_query = True):
        """ Execute the request """
        request = "SELECT * FROM (" + self.first_relation.execute(False)
        request += " NATURAL INNER JOIN " + self.second_relation.execute(False) + ")"

        # Create the table in the database
        self.database.execute_request(self.name, request)

        return super().edit_table_execute(is_last_query, True)

    def __str__(self):
        """ Transform the request into a string """
        return f"Join({self.first_relation}, {self.second_relation})"