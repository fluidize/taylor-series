import math
import sys

epsilon = sys.float_info.epsilon

# func
def f(x):
    return math.cos(x)

# TODO: clean up estimate_derivative function

# estimates derivative at x=0 using recursion
def estimate_derivative(function, degree):
   if (degree < 1):
       raise ValueError("Cannot find derivative of degree less than 1")

   if (degree == 1):
       return (function(0 + epsilon) - function(0 - epsilon))/(2*epsilon)
   else:
       return ((estimate_derivative(function, degree-1) + epsilon) - (estimate_derivative(function, degree-1) - epsilon))/(2*epsilon)
    
print(estimate_derivative(f, 1))