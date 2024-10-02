'''
The module will consist of pytest parametrize for string type a and b values along with operation
to be performed and the expected value. test method for the map_operate_print method.
'''
import pytest
from main import map_operate_print

@pytest.mark.parametrize("a_string, b_string, operation_string, expected_string", [
    ("5", "3", 'add', "The result of 5 add 3 is equal to 8"),
    ("10", "2", 'subtract', "The result of 10 subtract 2 is equal to 8"),
    ("4", "5", 'multiply', "The result of 4 multiply 5 is equal to 20"),
    ("20", "4", 'divide', "The result of 20 divide 4 is equal to 5"),
    ("1", "0", 'divide', "An error occurred: Cannot divide by zero"),
    ("9", "3", 'unknown', "Unknown operation: unknown"),
    ("a", "3", 'add', "Invalid number input: a or 3 is not a valid number."),
    ("5", "b", 'subtract', "Invalid number input: 5 or b is not a valid number.")
])

def test_map_operate_print(a_string, b_string, operation_string,expected_string, capsys):
    '''
    This function performs a test using pytest's capsys fixture to capture and verify
    the printed output from the map_operate_print function.
    '''
    map_operate_print(a_string, b_string, operation_string)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_string
