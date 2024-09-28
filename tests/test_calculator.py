'''My Calculator Test with Calculator instance'''
import pytest
from calculator import Calculator

def test_addition():
    '''Test that addition function works '''    
    assert Calculator.add(2,2) == 4

def test_subtraction():
    '''Test that addition function works '''    
    assert Calculator.subtract(2,2) == 0

def test_multiply():
    '''Test that addition function works '''    
    assert Calculator.multiply(2,2) == 4

def test_divide():
    '''Test that addition function works '''    
    assert Calculator.divide(2,2) == 1

def test_dividebyzero():
    '''Test that dividebyzero condition works'''
    with pytest.raises(ValueError, match="DivisionByZero exception occured"):
        Calculator.divide(2,0)
