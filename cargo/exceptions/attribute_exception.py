from cargo_exception import CargoException

class AttributeException(CargoException):
    attribute_name = ""

    def __init__(self, message, name):
        self.attribute_name = name
        self.message = message

    def __str__(self):
        return "Error: Attribute '" + self.attribute_name + "' not found"

    def log(self):
        pass