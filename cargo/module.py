from attribute import Attribute
import exceptions

class Module():
    """"Base class for exploits. Use this to implement an exploit"""
    target = Attribute(default="127.0.0.1", description="Target IP address.")
    silent = Attribute(default="false", description="Defines wether the exploit should run without printing anything.")

    attributes = dict([("target", target), ("silent", silent)])

    def __init__(self):
        pass

    def run(self):
        raise NotImplementedError("Error: 'run' method not defined in module!")

    def check(self):
        raise NotImplementedError("Error: 'check' method not defined in module!")

    def printInfo(self, message):
        if not self.getAttribute("silent") == "true":
            print "[*]" + message

    def printError(self, message):
        if not self.getAttribute("silent") == "true":
            print "[-]" + message

    def printSuccess(self, message):
        if not self.getAttribute("silent") == "true":
            print "[+]" + message

    def getAttribute(self, name):
        try:
            return self.attributes[name].data
        except KeyError:
            raise exceptions.AttributeException("Error: Attribute '" + name + "' not found", name)

    def setAttribute(self, name, data):
        try:
            self.attributes[name]
        except KeyError:
            raise exceptions.AttributeException("Error: Attribute '" + name + "' not found", name)
        self.attributes[name].data = data

    def addAttribute(self, name, data, description=""):
        self.attributes[name] = Attribute(data, description)

    def __str__(self):
        return self.__module__