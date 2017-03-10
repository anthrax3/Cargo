#!/usr/bin/env python2

from cargo import utils

version = "1.0.1"
author = "by Nick Aliferopoulos"
banner = """

   _____
  / ____|
 | |     __ _ _ __ __ _  ___
 | |    / _` | '__/ _` |/ _ \\
 | |___| (_| | | | (_| | (_) |
  \_____\__,_|_|  \__, |\___/
                   __/ |
                  |___/

"""

print banner
print version
print author

current = "null"

str = raw_input(">")
while not str == "quit" and not str == "exit":
    tokens = str.split(" ")
    if tokens[0] == "load":
        if not len(tokens) < 3:
            raise Exception("Error: Too many arguments")
        if not len(tokens) > 1:
            raise Exception("Error: Too few arguments")
        current = utils.import_cargo_module(tokens[1])()
    elif tokens[0] == "unload":
        # Unload the current module
        if not len(tokens) == 1:
            raise Exception("Error: Too many arguments")
        current = "null"
    elif tokens[0] == "set":
        # Set an attribute for the current module
        if not len(tokens) > 2:
            raise Exception("Error: Too many arguments")
        if not len(tokens) < 4:
            raise Exception("Error: Too few arguments")
        current.setAttribute(tokens[1], tokens[2])
    elif tokens[0] == "run":
        # Run the current module
        if not len(tokens) == 1:
            raise Exception("Error: Too many arguments")
        if current == "null":
            raise Exception("Error: No module loaded")
        current.run()
    elif tokens[0] == "check":
        # Check the current module
        if not len(tokens) == 1:
            raise Exception("Error: Too many arguments")
        if current == "null":
            raise Exception("Error: No module loaded")
        current.check()
    else:
        raise Exception("Error: Unknown command '" + tokens[0] + "'")
    if current == "null":
        str = raw_input(">")
    else:
        str = raw_input("(" + current.__str__() + ")" + ">")