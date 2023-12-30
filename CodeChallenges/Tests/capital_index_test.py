from unittest import TestCase
from capital_index import capital_indexes
import inspect


print(inspect.getmembers(unittest.TestCase))

class CapitalIndexTest(unittest.TestCase):
    def test_capital_indexes(self):
        input_string = 'Which way to Africa'
        expected_output = [0,13]
        output_string = capital_indexes(input_string)
           



