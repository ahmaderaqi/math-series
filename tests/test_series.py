from series import fibonacci
from series import lucas
from series import sum_series
def test_zero():
    actual=fibonacci(0)
    expeted=0
    assert actual==expeted

def test_one():
    actual=fibonacci(1)
    expeted=1
    assert actual==expeted

def test_two():
    actual=fibonacci(2)
    expeted=1
    assert actual==expeted

def test_three():
    actual=fibonacci(3)
    expeted=2
    assert actual==expeted

def test_four():
    actual=fibonacci(4)
    expeted=3
    assert actual==expeted

def test_five():
    actual=fibonacci(5)
    expeted=5
    assert actual==expeted

def test_six():
    actual=fibonacci(6)
    expeted=8
    assert actual==expeted

def test_ten():
    actual=fibonacci(8)
    expeted=21
    assert actual==expeted



def test_zero_lucas():
    actual=lucas(0)
    expeted=2
    assert actual==expeted

def test_lucas_one():
    actual=lucas(1)
    expeted=1
    assert actual==expeted

def test_lucas_two():
    actual=lucas(2)
    expeted=3
    assert actual==expeted

def test_lucas_three():
    actual=lucas(3)
    expeted=4
    assert actual==expeted

def test_lucas_four():
    actual=lucas(4)
    expeted=7
    assert actual==expeted

def test_lucas_five():
    actual=lucas(5)
    expeted=11
    assert actual==expeted

def test_lucas_six():
    actual=lucas(6)
    expeted=18
    assert actual==expeted

def test_lucas_ten():
    actual=lucas(8)
    expeted=47
    assert actual==expeted


def test_sum_ten():
    actual=sum_series(8)
    expeted=21
    assert actual==expeted

def test_sum_ten():
    actual=sum_series(0,2,1)
    expeted=2
    assert actual==expeted

