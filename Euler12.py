from itertools import count
from math import sqrt
from Util import prod

def countdivisors (x):
    numdivisors = 1

    currdiv = 2
    foo = x
    while currdiv < int(sqrt(foo) + 1):
        currpow = 0

        while foo % currdiv == 0:
            foo //= currdiv
            currpow += 1

        numdivisors *= currpow + 1
        currdiv += 1

    if foo != 1:
        # We have a prime left over
        numdivisors *= 2

    return numdivisors

def triangular():
    curr_val = 0
    for i in count(1):
        curr_val += i
        yield curr_val

for i in triangular():
    d = countdivisors(i)
    #print ((i, d))

    if d >= 100:
        print ((i, d))

    if d >= 500:
        break


# Split a number up into a dictionary of its divisors
def divisors (x):
    result = dict()

    foo = x
    currdiv = 2
    while currdiv <= foo:
        if foo % currdiv == 0:
            result[currdiv] = 0

        while foo % currdiv == 0:
            result[currdiv] += 1
            foo /= currdiv

        currdiv += 1
    return result
'''
for i in count(1):
    triag = i * (i + 1) // 2
    curr_div = divisors(i)
    next_div = divisors(i + 1)

    triangular_div = curr_div
    for i in next_div:
        if i in triangular_div:
            triangular_div[i] += next_div[i]
        else:
            triangular_div[i] = next_div[i]

    triangular_div[2] -= 1

    triangular_div_count = prod ( x + 1 for x in triangular_div.values() )

    # print (str(triag) + ' has ' + str(triangular_div_count) + ' divisors')

    if (triangular_div_count >= 500):
        print (triangular_div_count, triag)

'''
