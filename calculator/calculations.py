from decimal import Decimal
from typing import Callable, List
from calculator.calculation import Calculation

class Calculations:
    history: List[Calculation] = []#class variable to store the history of all calcilations

    @classmethod
    def add_calc(cls, calc: Calculation):
        
       # Add calculations to the history list
        
        cls.history.append(calc)

    @classmethod
    def get_calc(cls) -> List[Calculation]:
        
       # Returns the list of the calculations made
        
        return cls.history

    @classmethod
    def clear_calc(cls):
        
       # Clearing the history list using the clear method.
        
        cls.history.clear()

    @classmethod
    def get_latest_calc(cls) -> Calculation:
        
       # Retrives the latest history. Returns the most recent calculation if history exists or it will return None.
        
        if cls.history:
            return cls.history[-1]
        return None

    @classmethod
    def filter_by_operation(cls, operation_name: str) -> List[Calculation]:
        
       # Filters the operations that are matching the argument passed and returns the list of matching calculations.
        
        result = []
        for calc in cls.history:
            if calc.operation.__name__ == operation_name:
                result.append(calc)
        return result
