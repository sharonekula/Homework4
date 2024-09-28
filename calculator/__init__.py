from calculator.operations import add, subtract, divide, multiply
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from decimal import Decimal
from typing import Callable

class Calculator:
    @staticmethod
    def _perform(a: Decimal, b: Decimal, operation:Callable[[Decimal,Decimal], Decimal]) -> Decimal :
        calc = Calculation.createCalculation(a, b, operation)
        Calculation.add_calc(calc)
        return calc.perform()
    
    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform(a,b,add)
    
    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform(a, b, subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform(a ,b, multiply)
        
    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        Calculator._perform(a, b, divide)
