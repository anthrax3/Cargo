class Attribute():
    """"Represents an attribute that will be set by the user using 'set'. (e.g. 'set TARGET 127.0.0.1')"""
    def __init__(self, default, description=""):
        self.default = default
        self.description = description
        self.data = default
    def __get__(self, instance, owner):
        return self.data
    def __set__(self, instance, value):
        self.data = value