from cargo_exception import CargoException

class ModuleException(CargoException):
    module_name = ""

    def __init__(self, message, name):
        self.module_name = name
        self.message = message

    def __str__(self):
        return "Error: Could not load module '" + self.module_name + "'"

    def log(self):
        pass