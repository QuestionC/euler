from Util import is_prime
from itertools import combinations
from itertools import combinations_with_replacement
from itertools import permutations
from itertools import product

sequence = '1234567890'

for group_of_four in combinations_with_replacement(sequence, 4):
    primes = [ int(''.join(i)) for i in permutations(group_of_four) if i[0] != '0' and is_prime(int(''.join(i))) ]

    primes.sort()
    for x, y, z in combinations(primes, 3):
        if z - y == y - x and z - y != 0:
            print ( (x, y, z) )

