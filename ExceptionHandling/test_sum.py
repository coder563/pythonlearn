import unittest
from sum import sum
from fractions import Fraction
class SumTest(unittest.TestCase):


    def test_int_sum(self):
        val1 = 2
        val2 = 3
        self.assertEqual(sum(val1, val2),5)
        

    ###def test_fraction_sum(self):

    def test_fraction_sum(self):
        val1 = Fraction(2,8)
        val2 = Fraction(3,8)

        print(val1, val2, Fraction(5,8))
        self.assertEqual(sum(val1, val2),Fraction(5,8))


    def test_bad_input(self):
        val1 = 'banana'
        val2 = 2
        with self.assertRaises(TypeError):
            sum(val1,val2)







