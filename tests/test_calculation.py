from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

from decimal import Decimal
import pytest

@pytest.mark.parametrize("a, b, operation, expected", [
    (Decimal('5'), Decimal('5'), add, Decimal('10')),
    (Decimal('6'), Decimal('2'), subtract, Decimal('4')),
    (Decimal('2'), Decimal('5'), multiply, Decimal('10')),
    (Decimal('4'), Decimal('2'), divide, Decimal('2')),
    (Decimal('5.5'), Decimal('1.5'), add, Decimal('7.0')),
    (Decimal('6.4'), Decimal('2.4'), subtract, Decimal('4.0')),
])

def test_perform(a, b, operation, expected):
    calc = Calculation(a, b, operation)
    assert calc.perform() == expected, f"Failed performing the operation {operation.__name__}"

def test_strrepr():
    calc = Calculation(Decimal('4'), Decimal('2'), subtract)
    expected_str = "Calculation(4, 2, subtract)"
    assert calc.__str_repr__() == expected_str, "The string is not in correct format!"

def test_dividebyzero():
    calc = Calculation(Decimal('4'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="DivisionByZero exception occured."):
        calc.perform()
