class ModuleException(Exception):
    module_name = ""

    def __init__(self, name):
        self.module_name = name

    def log(self):
        pass