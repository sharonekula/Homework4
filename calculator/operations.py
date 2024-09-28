def add(a, b): 
   # Returns the sum of two numbers a and b.
    
   # Args:
      #  a: The first number.
       # b: The second number.
        
    #Returns:
       # The result of adding a and b.
    
    return a + b

def subtract(a,b): 
   # Returns the resulting of subtraction of two numbers a and b.
    
    #Args:
      #  a: The first number.
       # b: The second number.
        
   # Returns:
       # The result of subtraction a and b.
    
    return a - b

def multiply(a, b):
   # Returns the multiplication of two numbers a and b.
    
    #Args:
       # a: The first number.
       # b: The second number.
        
    #Returns:
       #The result of multiplication a and b.
    
    return a * b

def divide(a,b): 
    #Returns the division of two numbers a and b.
    
    #Args:
        #a: The first number.
       # b: The second number.
        
   # Returns:
        #The result of division of a and b.

    if b == 0 :
        raise ValueError("DivisionByZero exception occured.")
    else:
        return a / b
