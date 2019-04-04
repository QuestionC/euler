from Util import proper_divisors
from itertools import combinations_with_replacement
from math import sqrt

# All numbers greater than 28123 are the sum of two abundant numbers
abundants = set()
not_abundant_sum = 0

def factor(x):
    result = dict()

    curr_div = 2
    foo = x
    while curr_div < int(sqrt(foo) + 1):
        if foo % curr_div == 0:
            result[curr_div] = 0
        
        while foo % curr_div == 0:
            foo //= curr_div
            result[curr_div] += 1
        curr_div += 1

    if foo != 1:
        # We have a prime left over
        result[foo] = 1

    return result

def abundance(x):
    factors = factor(x)

    result = 1
    for i,j in factors.items():
        m = (i ** (j + 1) - 1) // (i - 1)
        result *= m
    return result - x

for i in range (1, 28124):
    # Is this number the sum of two abundants?
    for x in abundants:
        if i - x in abundants:
            break
    else:
        # We never hit x + y == i
        not_abundant_sum += i

    # Is this number abundant?
    if abundance(i) > i:
        abundants.add(i)

print (not_abundant_sum)

