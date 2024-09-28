from calculator.operations import add, subtract, divide, multiply
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from decimal import Decimal
from typing import Callable

class Calculator:
    @staticmethod
    def _perform(a: Decimal, b: Decimal, operation:Callable[[Decimal,Decimal], Decimal]) -> Decimal :
        # # Private procedure that takes two decimal numbers, a and b, and applies the given operation (add, subtract, multiply, divide).
        # With the given operation, it builds a Calculation object and adds it to the Calculations list.
        # returns the operation's outcome.

        # Arguments: a (Decimal): The operand that is used initially.
        # The operand that is second is b (Decimal).
        # The operation that needs to be carried out on a and b is operation (Callable[[Decimal, Decimal], Decimal]).

        # Returns: Decimal: The outcome of the process

        calc = Calculation.createCalculation(a, b, operation)
        Calculations.add_calc(calc)
        return calc.perform()
    
    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        #Performs addition on two decimal values a and b
        return Calculator._perform(a,b,add)
    
    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:#Performs subtraction on two decimal values a and b
        return Calculator._perform(a, b, subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:#Performs multiplication on two decimal values a and b
        return Calculator._perform(a ,b, multiply)
        
    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:#Performs division on two decimal values a and b
        return Calculator._perform(a, b, divide)
