# 197 is a circular prime because all rotations of the digits 197, 971, and 719, are prime.

# How many circular primes are there below one million?

# Primes can't end with 5 or 0, so disregard those
# Primes can't end with even numbers, so disregard those
digits = ['1', '3', '7', '9']

import itertools
import Util

count = 0

for length in range (1, 7):
    for curr_val in itertools.product(digits, repeat = length):
        for rotate_amount in range(length):
            curr_rotation = itertools.islice(itertools.cycle(curr_val), rotate_amount, rotate_amount + length)
            i = int(''.join(curr_rotation))
            if not Util.is_prime(i):
                break
        else:
            print (curr_val)
            count += 1

print (count)
