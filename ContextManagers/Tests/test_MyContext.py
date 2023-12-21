import unittest
import MyContext
class MyContextTest(unittest.TestCase):

    def test_context_creation(self):
       
       ctx = MyContext()
       print("Created Context")

       with ctx as obj:
         print("Inside the WithBlock ", obj)
         raise ValueError()
       
       self.assertEquals(obj,True)



