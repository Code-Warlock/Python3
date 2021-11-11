""" More on Python Functions """
import math
#  Recursive functions
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)

def factorial(n):
    return math.factorial(n)
# print(factorial(5))
# LEGB Scoping in Python


def print_test():
    """ Higher Order Function """
    x = 5
    def mult():
        """ Lower Order Function """
        return x * 12
    return mult()
# print(print_test())

def area(l , b):
    """ Area function """
    return l * b


def volume(area , h):
    """ Volume function """
    return area * h





print(f"Area of rectangle : {area(5,3, 7)} ")
volume_of_rect = volume(area(5,3), 7)
print(f"Volume of Rectangle : {volume_of_rect}")
