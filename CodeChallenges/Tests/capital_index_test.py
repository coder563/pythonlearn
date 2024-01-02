import unittest
from capital_index import capital_indexes

 
class CapitalIndexTest(unittest.TestCase):
    def test_capital_indexes(self):
        input_string = 'Which way to Africa ? I dont know'
        expected_output = [0,13,22]
        output = capital_indexes(input_string)
        
        print('inside capitalindextest')
        self.assertEqual(expected_output,output)


 
if __name__ == '__main__':
    unittest.main()