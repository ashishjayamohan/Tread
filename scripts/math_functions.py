import math

def add_num(a, b):
    """
    Given two numbers, this function will return the sum of these
    Will be returned in whichever type input is given (int, float)
    """
    return a + b

def subtract_num(a, b):
    """
    Given two numbers, this function will deduct the second number from the first
    Returned numerical's type is of input's type
    """
    return a - b

def abs_diff(a, b):
    """
    Given two numbers, this function will return the absolute difference between the two
    """
    return abs(a - b)

def easter():
    # Le Undocumented Function
    print("Wow, you found this.")
    print("Good job, I just wasted 2 seconds of your time.")
    print("-----------------------------------------------")

def divide_num(a, b):
    """
    Given two number, this function will return the first number divided by the second
    Returned numerical's type is a float
    """
    if(b == 0):
        raise TypeError("Divide by Zero Not Allowed")
    else:
        return a/b

def multiply_num(a, b):
    """
    Given two numbers, this function will return the product of the two
    """
    return a * b

def mod(a, b):
    """
    Given two numbers, this function will return the first number modulo the second number
    """
    return a % b

def factorial(n):
    """
    Given a singular number, this function will return the factorial of the number
    """
    return math.factorial(n)

def choose(a, b):
    """
    Given two numbers, this function will return the first number choose the second number
    """
    return (factorial(a))/(factorial(b)*factorial(abs(a-b)))
