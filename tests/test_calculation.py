#Module Docstring unit tests for the calculation class and its operations(add,sub,mul,div) are included in this module.For parameterized testing pytest is used
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide


#Parametrized test for add,sub,mul,div
@pytest.mark.parametrize("n1, n2, operation, expected", [
    (Decimal('5'), Decimal('5'), add, Decimal('10')),
    (Decimal('6'), Decimal('2'), subtract, Decimal('4')),
    (Decimal('2'), Decimal('5'), multiply, Decimal('10')),
    (Decimal('4'), Decimal('2'), divide, Decimal('2')),
    (Decimal('5.5'), Decimal('1.5'), add, Decimal('7.0')),
    (Decimal('6.4'), Decimal('2.4'), subtract, Decimal('4.0')),
])

def test_perform(n1, n2, operation, expected):
    '''
    method docstring
    
    This test function generates a Calculation object and verifies that the operation's outcome (carried out by `calc.perform()}) corresponds to what was anticipated.
    
    Args: n1 (Decimal): The operand that comes first.
        (Decimal) n2: The operand that is second.
        operation (Callable): The addition, subtraction, multiplication, and division of a mathematical operation.
        expected (Decimal): The anticipated outcome of the procedure.
    '''
    calc = Calculation(n1, n2, operation)
    assert calc.perform() == expected, f"Failed performing the operation {operation.__name__}"

def test_strrepr():
    '''
    method docstring
     Using `__str_repr__}, this test function checks if the string representation of a Calculation object is formatted correctly.
    
    The formula "Calculation(a, b, operation_name)" is what is anticipated.
    '''
    calc = Calculation(Decimal('4'), Decimal('2'), subtract)
    expected_str = "Calculation(4, 2, subtract)"
    assert calc.__str_repr__() == expected_str, "The string is not in correct format!"

def test_dividebyzero():
    '''
    method-docstring
    This test function determines whether division by zero results in the ValueError exception with the message "DivisionByZero exception occurred."
    
    It uses the `raises} function from pytest to check for the relevant exception after creating a Calculation object with a zero divisor.
    '''
    calc = Calculation(Decimal('4'), Decimal('0'), divide)#Create a calculation object for division by zero
    with pytest.raises(ValueError, match="DivisionByZero exception occured."):
        calc.perform()
