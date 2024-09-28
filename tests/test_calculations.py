'''
module-docstring
'''
from decimal import Decimal
import pytest

from calculator.calculations import Calculations
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

@pytest.fixture
def set_calc():
    '''
    method docstring
    '''
    Calculations.clear_calc()

    Calculations.add_calc(Calculation(Decimal('5'), Decimal('2'), add))
    Calculations.add_calc(Calculation(Decimal('5'), Decimal('2'), subtract))
    Calculations.add_calc(Calculation(Decimal('4'), Decimal('2'), multiply))
    Calculations.add_calc(Calculation(Decimal('4'), Decimal('2'), divide))

def test_add_calc(set_calc):
    '''
    method-docstring
    '''
    calc = Calculation(Decimal('3'), Decimal('2'), add)
    Calculations.add_calc(calc)
    assert Calculations.get_latest_calc() == calc, "History addition failed"

def test_get_calc(set_calc):
    '''
    method-docstring
    '''
    history = Calculations.get_calc()
    assert len(history) == 4, "Number of values in History is not correct"

def test_clear_calc(set_calc):
    '''
    method-docstring
    '''
    Calculations.clear_calc()
    assert len(Calculations.get_calc()) == 0, "History is not cleared"

def test_get_latest_calc(set_calc):
    '''
    method-docstring
    '''
    latest_calc = Calculations.get_latest_calc()
    assert latest_calc.a == Decimal('4') and latest_calc.b == Decimal('2'), "Latest calculation is not correct"

def test_filter_by_operation(set_calc):
    '''
    method-docstring
    '''
    test_add = Calculations.filter_by_operation("add")
    test_subtract = Calculations.filter_by_operation("subtract")
    assert len(test_add) == 1, "Addition calculation count is not correct"
    assert len(test_subtract) == 1, "SUbtraction calculation count is not correct"

def test_getlatestwhenempty():
    '''
    method-docstring
    '''
    Calculations.clear_calc()
    assert Calculations.get_latest_calc() is None, "None value is Expected but history is not empty"
