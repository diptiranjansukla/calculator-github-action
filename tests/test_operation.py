from src.math import add,sub,mul

def test_add():
    assert add(2,3)==5
    assert add(4,3)==7
    assert add(1,3)==4

def test_sub():
    assert sub(3,3)==0
    assert sub(8,3)==5
    assert sub(9,3)==6


def test_mul():
    assert mul(3,3)==9
    assert mul(8,3)==24
    assert mul(9,3)==27


