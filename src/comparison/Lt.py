from comparison.Eq import Eq

class Lt(Eq):
    """ Represents a less than operation between an attribute and a value

    Attributes:
        name_attribute      name of the attribute to compared with the value
        value               value to compared to the attribute's value
        operator            operator for this comparison
    """

    def __init__(self, name_attribute, value):
        super().__init__(name_attribute, value)
        self.operator = "<"

    def __str__(self):
        """ Transform the request into a string """
        return f"Gt('{self.name_attribute}', '{self.value}')"