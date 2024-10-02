'''Testing Operations Module'''
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide


def test_operation_add():
    '''Addition operation test '''
    calculation = Calculation(Decimal('2'), Decimal('2'), add)
    assert calculation.perform() == Decimal('4'), "Error! Addition operation"

def test_operation_subtract():
    '''Subtract operation test'''
    calculation = Calculation(Decimal('7'), Decimal('5'), subtract)
    assert calculation.perform() == Decimal('2'), "Error in Subtract operation"

def test_operation_multiply():
    '''Multiplication operation test'''
    calculation = Calculation(Decimal('5'), Decimal('5'), multiply)
    assert calculation.perform() == Decimal('25'), "Error in Multiply operation"

def test_operation_divide():
    '''Division operation test'''
    calculation = Calculation(Decimal('12'), Decimal('2'), divide)
    assert calculation.perform() == Decimal('6'), "Error in Divide operation"

def test_divide_by_zero():
    '''Testing the divide by zero exception'''
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation = Calculation(Decimal('5'), Decimal('0'), divide)
        calculation.perform()
