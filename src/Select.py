class Select:
    """ Represent a SELECT request (SPJRUD)

    Attributes:
        comparison  condition of selection (equality, ...)
        relation    the relation on which perform the comparison
    """

    def __init__(self, comparison, relation):
        self.comparison = comparison
        self.relation = relation

        # The attribute to compared has to be in the relation
        if not comparison.name_attribute in relation.database_schema:
            raise Exception("Attribut is not in the relation")