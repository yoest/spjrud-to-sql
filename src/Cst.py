class Cst:
    """ This class is used to keep a constant value 
    
    Attributes:
        value   constant value to keep
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        """ Transform the request into a string """
        return f"Cst('{self.value}')"