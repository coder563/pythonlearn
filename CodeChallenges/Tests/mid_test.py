import unittest
from mid import mid


class MiddleLetterTest(unittest.TestCase):
    def test_middle_letter(self):
        test_input = "World_Cup"
        expected_mid = 'd'
        actual_mid = mid(test_input)
         
        self.assertEqual(expected_mid,actual_mid)



if __name__ == '__main__':
    unittest.main()