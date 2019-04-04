from math import sqrt
from itertools import count

def is_prime(i):
    if i % 2 == 0: return i == 2

    for j in range (3, int(sqrt(i) + 1), 2):
        if i % j == 0:
            return False
    return True

def primes():
    yield 2

    test_me = 3
    for i in count(3, 2):
        for j in range(3, int(sqrt(i) + 1), 2):

            if i % j == 0:
                break
        else:
            yield i

def next_primes(N):
    if N == 2:
        yield 2

    if N % 2 == 0:
        N += 1

    for i in count(N, 2):
        for j in range(3, int(sqrt(i) + 1), 2):
            if i % j == 0:
                break
        else:
            yield i

def proper_divisors(x):
    for i in range (1, x):
        if x % i == 0:
            yield i

def prod (x):
    curr = 1
    for i in x:
        curr *= i
    return curr

def factor(x):
    curr_div = 2
    foo = x
    while curr_div < int(sqrt(foo) + 1):
        power = 0
        while foo % curr_div == 0:
            power += 1
            foo //= curr_div
        if power != 0:
            yield curr_div, power
        curr_div += 1

    if foo != 1:
        # We have a prime left over
        yield foo, 1

def gcd (a, b):
    x = max(a, b)
    y = min(a, b)


    while y != 0:
        z = x % y
        x = y
        y = z

    return x

def lcm (a, b):
    return a * b // gcd(a, b)

import heapq

# Return the value (function(x,y), x, y) such that test(x,y) is true and 
#  function(x,y) is as small as possible.
# function(x, 1) must be monotonically increasing w/r to x
# function(k, y) must be monotonically increasing w/r to y
def minimum (function, test, start = (1, 1)):
    heap = []
    heapq.heappush (heap, (function(*start), start))

    pair = (start[0] + 1, 1)
    next_tier = (function(*pair), pair)

    while True:
        # Too expensive to pop here
        # top = heapq.heappop(heap)
        top = heap[0]


        a = top[1][0]
        b = top[1][1]
     
        if a > 100000:
            print (top)
        
        if test(*top[1]):
            return top

        # Add the next value within this tier
        pair = (a, b + 1)
        
        # heapq.heappush(heap, (function(*pair), pair))
        heapq.heapreplace(heap, (function(*pair), pair))

        # Add any higher tiers which have qualified
        while (top > next_tier):
            heapq.heappush(heap, next_tier)
            
            a = next_tier[1][0]
            b = next_tier[1][1]

            pair = (next_tier[1][0] + 1, )
            next_tier = (function(*pair), pair)
