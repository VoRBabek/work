import pytest 
#adadadad
def plus(a,b):
    return a+b

def minus(a,b):
    return a-b

def test_plus():
    assert plus(1, 2) == 3 

def test_minus():
    assert minus (1,2) == -1
