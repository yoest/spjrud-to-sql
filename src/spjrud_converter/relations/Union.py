from spjrud_converter.relations.Rel import *

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
        super().__init__(self.first_relation.name + "_" + self.second_relation.name + "_uni", self.perform(), False)

    def perform(self):
        """ Perform the union request to get the new schema """
        return self.first_relation.database_schema

    def check_request(self):
        """ Both relations has to have the same attributes """
        has_same_attributes = True
        for attribute in self.first_relation.database_schema:
            if not attribute in self.second_relation.database_schema:
                has_same_attributes = False

        has_same_size = len(self.first_relation.database_schema) == len(self.second_relation.database_schema)

        if not has_same_attributes or not has_same_size:
            error_request = f"\n\nInvalid expression.\nThe (sub-)expression\n\t{self}\nis invalid because the schema of\n\t{self.first_relation}\nwhich is\n\t{self.first_relation.database_schema}\nis not the same as the schema of\n\t{self.second_relation}\nwhich is\n\t{self.second_relation.database_schema}"

            raise ValueError(error_request)

    def execute(self, is_last_query = True):
        """ Execute the request """
        request = "SELECT * FROM " + self.first_relation.execute(False)
        request += " UNION "
        request += "SELECT * FROM " + self.second_relation.execute(False)

        # Create the table in the database
        self.database.execute_request(self.name, request)

        return super().edit_table_execute(is_last_query, True)

    def __str__(self):
        """ Transform the request into a string """
        return f"Union({self.first_relation}, {self.second_relation})"