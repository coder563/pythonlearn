
from inc_dec import increment
from inc_dec import decrement


def test_increment():
    assert increment(3) == 4 

def test_decrement():
    assert decrement(3) == 2