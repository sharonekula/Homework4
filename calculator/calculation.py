from calculator.operations import add, subtract, multiply, divide
from typing import Callable
from decimal import Decimal

class Calculation:
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        self.a = a
        self.b = b
        self.operation = operation

    @staticmethod
    def createCalculation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        return Calculation(a, b, operation)

    def perform(self) -> Decimal:
        return self.operation(self.a, self.b)

    def __str_repr__(self):
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"