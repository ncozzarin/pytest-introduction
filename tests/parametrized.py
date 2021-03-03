import pytest

# Multiplication test ideas

"""
two positive integers
identity: multiply any number by 1
zer: mulptiply by 0
negative by negative
positive by positive
multiply floats

"""

def test_multiply_two_positive_ints():
    assert 2 * 3 == 6

def test_multiply_identity():
    assert 1 * 99 == 99

def test_multiply_zero():
    assert 0 * 100 == 0

#This is a bad practice as i am repeating the tests, what should be user is pytest mark parametrize
# Parametrized test function:
products = [
    (2,3,6),             # positive integers
    (1,99,99),           # identity
    (3,-4,-12),          # positive by negative
    (-5,-5,25),          # negative by negative
    (2.5,6.7,16.75),     # floats
]

@pytest.mark.parametrize('a,b,product',products)
def test_multiplication(a,b,product):
    assert a * b == product