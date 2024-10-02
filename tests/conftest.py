'''
This module creates test data for addition, subtraction, multiplication, and division using the Faker library. 
Plus, it offers the ability to change the quantity of test cases using the pytest command-line arguments.
'''
from decimal import Decimal
from faker import Faker
from calculator.operations import add, subtract, multiply, divide

fake = Faker()

def generate_test_records(num_of_records):
    '''
    Generates test records for arithmetic operations using random numbers and operations.
    '''
    opr_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }
    for _ in range(num_of_records):
        a = Decimal(fake.random_number(digits=2))
        b = Decimal(fake.random_number(digits=2)) if _ % 4 != 3 else Decimal(fake.random_number(digits=1))
        opr_name = fake.random_element(elements=list(opr_mappings.keys()))
        operation_func = opr_mappings[opr_name]
        if str(operation_func.__name__) == "divide":
            b = Decimal('1') if b == Decimal('0') else b
        try:
            if str(operation_func.__name__) == "divide" and b == Decimal('0'):
                expected = "ZeroDivisionError"
            else:
                expected = operation_func(a, b)
        except ZeroDivisionError:
            expected = "ZeroDivisionError"
        yield a, b, opr_name, operation_func, expected

def pytest_addoption(parser):
    '''
    Adds a command-line option for pytest to specify the number of test records.
    '''
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    '''
    Parametrizes test functions with generated test data based on the pytest command-line option.
    '''
    if {"a", "b", "expected"}.intersection(set(metafunc.fixturenames)):
        num_of_records = metafunc.config.getoption("num_records")
        parameters = list(generate_test_records(num_of_records))
        _parameters = [(a, b, op_name if 'opr_name' in metafunc.fixturenames else op_func, expected) for a, b, op_name, op_func, expected in parameters]
        metafunc.parametrize("a,b,operation,expected", _parameters)
