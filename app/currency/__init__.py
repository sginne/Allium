from . import *
import glob, os, importlib
class FiatCurrency:
    module=None
    def __init__(self,module_in_config):
        import importlib
        #module_files = glob.glob(os.path.join(os.path.dirname(__file__), "*.py"))
        #print(module_files)
        #item_name=(module_files[1])
        #print(item_name)
        item=importlib.import_module("app.currency."+module_in_config)
        what=item.FiatCrypto
        coin=what()
        self.module=coin
        #print(importlib.util.find_spec(module_in_config))



