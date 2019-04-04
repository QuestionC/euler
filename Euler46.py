from itertools import count
from Util import is_prime

# Find the lowest non-prime odd which can not be written as the sum of a prime and twice a squarei

primes = [2] # 2 won't come up, but doesn't really hurt either

for i in count(3, 2):
    if is_prime(i):
        print (i)
        primes.append(i)
    else:
        for p in primes:
            for k in count(1):
                if i <= p + 2 * k * k:
                    break
            if i == p + 2 * k * k:
                print ((str(i), p, k))
                break

        else:
            # We exhausted every prime without finding a value that satisfies i = p + 2kk
            print ( 'Answer = ' + str(i) )
            break
