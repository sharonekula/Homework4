'''
module-docstring Unit tests for the `Calculations` class from the calculator package are included in this module. 
Tests are included for adding, retrieving, cleaning, and filtering calculations.
 Special circumstances are also covered such as getting the most recent calculation in the event that the history is empty.
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
    Before doing each test  use the fixture method to initialize the computation history.
    By doing this it is ensured that before adding predefined calculations for testing, the {Calculations` history is cleared.

      Adds the following calculations to the history:
        - 5 + 2
        - 5 - 2
        - 4 * 2
        - 4 / 2
    '''
    Calculations.clear_calc()#clear the history before setting up
#Adding some predefined calculations to the history
    Calculations.add_calc(Calculation(Decimal('5'), Decimal('2'), add))
    Calculations.add_calc(Calculation(Decimal('5'), Decimal('2'), subtract))
    Calculations.add_calc(Calculation(Decimal('4'), Decimal('2'), multiply))
    Calculations.add_calc(Calculation(Decimal('4'), Decimal('2'), divide))

def test_add_calc(set_calc):
    '''
    method-docstring Test for adding a new calculation to the history.
    It adds a new calculation (3 + 2) and asserts that the latest calculation in history matches the one added.
    '''
    calc = Calculation(Decimal('3'), Decimal('2'), add)
    Calculations.add_calc(calc)
    assert Calculations.get_latest_calc() == calc, "History addition failed"

def test_get_calc(set_calc):
    '''
    method-docstring
    Test for retrieving the list of calculations from the history.
    Asserts that the history contains the expected number of calculations (4).
    '''
    history = Calculations.get_calc()
    assert len(history) == 4, "Number of values in History is not correct"

def test_clear_calc(set_calc):
    '''
    method-docstring
     Test for clearing the calculation history.
    After clearing the test asserts that the history length is zero.
    '''
    Calculations.clear_calc()
    assert len(Calculations.get_calc()) == 0, "History is not cleared"

def test_get_latest_calc(set_calc):
    '''
    method-docstring
    Test for retrieving the most recent calculation from the history.
    The test asserts that the latest calculation's operands are 4 and 2 which corresponds to the last calculation added.
    '''
    latest_calc = Calculations.get_latest_calc()
    assert latest_calc.a == Decimal('4') and latest_calc.b == Decimal('2'), "Latest calculation is not correct"

def test_filter_by_operation(set_calc):
    '''
    method-docstring
    Test for filtering calculations by the operation type.
    The test asserts that there is exactly 1 addition and 1 subtraction calculation in the history.
    '''
    test_add = Calculations.filter_by_operation("add")
    test_subtract = Calculations.filter_by_operation("subtract")
    assert len(test_add) == 1, "Addition calculation count is not correct"
    assert len(test_subtract) == 1, "SUbtraction calculation count is not correct"

def test_getlatestwhenempty():
    '''
    method-docstring
    Test for retrieving the latest calculation when the history is empty.
    After clearing the history the test asserts that `get_latest_calc()` returns None.
    '''
    Calculations.clear_calc()
    assert Calculations.get_latest_calc() is None, "None value is Expected but history is not empty"
