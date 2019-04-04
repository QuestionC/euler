# Project Euler Problem 44

# Pentagonal numbers have the form Pn = n * (3*n - 1) / 2
# eg, 1, 5, 12, 22, 35, &ct

# Find a pair of pentagonal numbers for which their sum and difference is pentagonal
# With the smallest difference

# What is their difference?

# Do the math and it works out that when (3*L - 1)*L == (3*(b + a) - 1)*(b - a), we have a match for the difference where pentag(L) is the difference and pentag(a) and pentag(b) are the pentagonal values
# So then we just have to test if their sum is pentagonal


import math
import itertools

def pentag(n):
    return n * (3*n - 1) // 2

def ispentag(x):
    if x <= 0:
        return None
    # Use binomial theorum to solve Pentag formula
    low_float = (1 + math.sqrt(24 * x)) / 6
    n = math.ceil(low_float)
    if x == pentag(n):
        return n
    else:
        return None

# find the (x, y) such x + y is prime and sq(x) - sq(y) is minimized
import Util
print (
        Util.minimum (
            lambda a, b: (a+b)*(a+b) - a*a, 
            lambda a, b: Util.is_prime(a + a + b),
            (3, 3)
            )
        )

# Find the (x, y) such that pentag(x) + pentag(y) is pentag and 
#  pentag(x) - pentag(y) is pentag minimizing
#  pentag(x) - pentag(y)
#  
print (
        Util.minimum (
            lambda a, b: pentag(a + b) - pentag(a),
            lambda a, b: 
                ispentag(pentag(a + b) + pentag(a)) and 
                ispentag(pentag(a + b) - pentag(a))
            )
        )
'''
print (
        Util.minimum (
            lambda a, b: 2*pentag(a) - pentag(a + b),
            lambda a, b: 
                ispentag(2*pentag(a) - pentag(a + b)) and
                ispentag(pentag(a + b) - pentag(a))
                   ) 
        )
'''
