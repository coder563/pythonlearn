from dataclasses import dataclass
class Circle:


    def __init__(self,x, y , radius) -> None:
        
        self.x:int = x
        self.y:int = y
        self.radius:int = radius 


    def __repr__(self):
        return f'{self.__class__.__qualname__} with x={self.x}, y={self.y}, radius={self.radius}'

    def __hash__(self):
        return hash(( self.x,self.y,self.radius))
    
    def __eq__(self, __value: object) -> bool:
        if self.__class__ == __value.__class__:
            return (self.x, self.y, self.radius) == (__value.x, __value.y, __value.radius)
        else:
            print(f'bool value of NotImplemented ={NotImplemented.__bool__()}') 
            print(f'bool value of NotImplemented ={NotImplemented.__value__}') 
            return NotImplemented
@dataclass(frozen=True)
class CircleD:
    x:int
    y:int
    radius:int



if __name__ =='__main__':
    c1 = CircleD(3,4, 10)
 
    c2 = CircleD(3,5,10)
    
    c3 = CircleD(3,4,10)

    print(f'ID c1 ,c2, c3 = {id(c1)} {id(c2)} {id(c3)}')
    print(f'Hashes c1 ,c2, c3 = {hash(c1)} {hash(c2)} {hash(c3)}')




















 
    