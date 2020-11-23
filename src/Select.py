class Select:
    """ Represent a SELECT request (SPJRUD)

    Attributes:
        comparison  condition of selection (equality, ...)
        relation    the relation on which perform the comparison
    """

    def __init__(self, comparison, relation):
        self.comparison = comparison

        self.initial_relation = relation
        self.relation = relation.request_relation

        # The attribute to compared has to be in the relation
        if not self.comparison.name_attribute in self.relation.database_schema:
            raise Exception("Attribut is not in the relation")

        # Perform the request
        self.request_relation = self.perform()

    def perform(self):
        """ Perform the select request to get the new relation """
        return self.relation

    def __str__(self):
        """ Transform the request into a string """
        return f"Select({self.comparison}, {self.initial_relation})"