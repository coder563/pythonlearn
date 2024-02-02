import Circle as c
import Dataclasses.Circle as dc 

def test_count():
    assert 4, 5+1




def test_circle_properties():
    
    dc.Circle(2,2,2)
    c1 = c.Circle(8,4,3)

    c1.radius = 10

    assert 10 , c1.radius



