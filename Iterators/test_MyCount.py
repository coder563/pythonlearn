import unittest
from  MyCount import MyCount


class MyCountTest(unittest.TestCase):

    def test_first_item(self):
            
            it1=iter(MyCount(start =4,step = 5, end=20))
            first_item = it1.__next__()
            print(self.assertEqual(first_item,4))
                     
                  
                
    
    def test_last_item(self):
                
            it1 = iter(MyCount(start = 4,step = 5, end=29))
 
            for item in it1:
          
                if item == 29:            
                   with  self.assertRaises(StopIteration):
                        it1.__next__()     
                  

    def test_step(self):
            step = 5
            it1 = iter(MyCount(start=4,step=step,end=29))

            item1 = it1.__next__()
            item2 = it1.__next__()
            item3 = it1.__next__()

            self.assertTrue( (item2-item1 == 5 and item3-item2 ==5))

                  

                  


if __name__ == '__main__':
    unittest.main()
          





