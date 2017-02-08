import os

from textXGrammar import execute as ex
from textXGrammar import rentalcars as rc


query_set = ex.execute(os.path.split(__file__)[0], 'grammar.tx', 'test.query', True, True)

html_response = rc.make_requests(query_set)

print(html_response)
