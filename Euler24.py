total = 1000000

from math import factorial

digits = list( range(10) )

# Bug: Subtract 1 from total since we count from 0
total -= 1

while len(digits) != 0:
    fact = factorial (len(digits) - 1)
    offset = int(total / fact)

    print (str(digits.pop(offset)))
    total -= offset * fact

