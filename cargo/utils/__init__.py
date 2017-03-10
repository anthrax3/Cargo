#from __future__ import absolute_import

import os
import importlib
from .. import modules as cargo_modules

DIRECTORY_MODULES = cargo_modules.__path__[0]
DIRECTORY_EXPLOITS = os.path.join(DIRECTORY_MODULES, 'exploits')

def import_cargo_module(path):
    """" Imports a Cargo module
    :param path: Python-formatted path to the module (e.g. cargo.modules.scanners.multi.tcp_port_scan
    :return: Module or error if module does not exist or cannot be imported.
    """
    try:
        module = importlib.import_module(path)
        return getattr(module, "Module")
    except(ImportError, AttributeError, KeyError) as error:
        raise Exception(error)
