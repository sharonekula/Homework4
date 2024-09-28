from calculator.operations import add, subtract, multiply, divide
from typing import Callable
from decimal import Decimal

class Calculation:
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]): 
        #Intializes a new calculation with an action to be performed on two decimal operands(a and b)
        #Arguments: a(Decimal): The operand that is used intially.
        #The operanf that is second is b(Decimal).
        #Collab[[Decimal,Decimal],Decimal]] operation: The operations(multiply,divide,subtract,add) in mathematics.
        self.a = a #Store the first operand
        self.b = b #Store the second operand
        self.operation = operation #Store the operation function

    @staticmethod
    def createCalculation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]): 
# A static method that builds and returns a new Calculation object is called 

# Arguments: a (Decimal): The operand that is used initially.
# The operand that is second is b (Decimal).
# The operation that has to be carried out is operation (Callable[[Decimal, Decimal], Decimal]).

# Returns: Calculation: A fresh instance of the Calculation object.

        return Calculation(a, b, operation)

    def perform(self) -> Decimal:
         #Executes the stored operation on the two operands (a and b) and returns the result. Returns: Decimal: The result of the operation.
        return self.operation(self.a, self.b)

    def __str_repr__(self):# Returns a string representation of the Calculation object that displays the operation's name and operands.
        
       # Returns: str: The Calculation object represented as a string 
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"