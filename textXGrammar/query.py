import os

from textXGrammar import execute as ex


ex.execute(os.path.split(__file__)[0], 'grammar.tx', 'test.query', True, True)