import unittest
from Aggregates import Order 
class OrderAggregateTest(unittest.TestCase) :


    def test_should_create_order(self):
        order = Order.create_order(1)

        self.assertEqual(order,OrderCreated)


  




    







