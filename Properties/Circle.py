import math
import pprint
class Circle:


    def __init__(self,radius) -> None:
        self.__radius = radius



    @property
    def radius(self):
        'get the radius'
        return self.__radius
    

    @radius.setter
    def radius(self, radius):
        print('Set radius')
        self.__radius = radius
  

    @radius.deleter
    def radius(self,radius):
        print('Delete radius')
        del self.__radius
        
    


if __name__ == '__main__':
    c1 = Circle(49)
    c1.radius = 20
    print(f'{c1.radius=}')


#    pprint.pprint(getattr(Circle.__dict__['radius'],'setter'))
   # print(type(dir(Circle.radius)[-1]))
  #  print(f'{c1.radius=}')
   # c1.radius = 42
   # print(f'{c1.radius=}')
          