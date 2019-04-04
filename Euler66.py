import math
import itertools
import Util

best = (0, None)

solved = set()

# True if X is a perfect square.  False otherwise
def perfectSquare(x):
    return x == int(math.sqrt(x))**2

# All numbers can be expressed as a*b*b for some maximal b
def nonSquare(x):
    result = 1
    curr = x
    for i in itertools.count(2):
        while curr % i == 0:
            curr //= i
            if curr % i == 0:
                curr //= i
            else:
                result *= i
        if curr == 1:
            return result

def solveX1 (D):
    for y in itertools.count(1):
        x_sq = D * y * y + 1
        if perfectSquare(x_sq):
            return (y, x_sq)

def solveX2 (D):
    if perfectSquare(D + 1):
        return D + 1
    for i in itertools.count(1):
        y_sq = i * i * D - 2 * i
        print (D * y_sq + 1)
        if (perfectSquare(y_sq)):
            x_sq = D * y_sq + 1
            if not perfectSquare(x_sq):
                print ("NO")
                exit()
            return x_sq

        y_sq = i * i * D + 2 * i
        if (perfectSquare(y_sq)):
            x_sq = D * y_sq + 1
            if not perfectSquare(x_sq):
                print ("NO")
                exit()
            return x_sq


for D in Util.primes():
    if D >= 1000: break
    if D < 250: continue
    print (D)
    if perfectSquare(D): continue

    # This is the trick!
    # if nonSquare(D) * 4 < 1000: continue

    x_sq= solveX2(D)
    print ((x_sq, D))
    if x_sq > best[0]:
        best = ((x_sq, D))

print (best)
