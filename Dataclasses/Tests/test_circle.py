import Circle 


def test__eq__():

  c1 , c2 = Circle(3, 4, 5), Circle(2,4,5)
  print('Am in test__eq')
  assert c1.__eq__(c2)




if __name__ == '__main__':
   print('Inside main')
   test__eq__()
  


