class Eq:
    """ Represents an equality between an attribute and a value

    Attributes:
        name_attribute      name of the attribute to compared with the value
        value               value to compared to the attribute's value
    """

    def __init__(self, name_attribute, value):
        self.name_attribute = name_attribute
        self.value = value

    def __str__(self):
        """ Transform the request into a string """
        return f"Eq('{self.name_attribute}', '{self.value}')"