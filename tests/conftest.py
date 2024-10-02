import pytest
from decimal import Decimal
from faker import Faker
from calculator.operations import add, subtract, multiply, divide

fake = Faker()

def generate_test_records(num_of_records):
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
        if operation_func == divide:
            b = Decimal('1') if b == Decimal('0') else b
        try:
            if operation_func == divide and b == Decimal('0'):
                expected = "ZeroDivisionError"
            else:
                expected = operation_func(a, b)
        except ZeroDivisionError:
            expected = "ZeroDivisionError"
        
        yield a, b, opr_name, operation_func, expected

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    if {"a", "b", "expected"}.intersection(set(metafunc.fixturenames)):
        num_of_records = metafunc.config.getoption("num_records")
        parameters = list(generate_test_records(num_of_records))
        _parameters = [(a, b, op_name if 'opr_name' in metafunc.fixturenames else op_func, expected) for a, b, op_name, op_func, expected in parameters]
        metafunc.parametrize("a,b,operation,expected", _parameters)