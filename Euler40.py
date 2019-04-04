# Project Euler problem 40

'''
An irrational decimal fraction is created by concatenating the positive integers:
0.123456789101112131415161718192021...
It can be seen that the 12th digit of the fractional part is 1.
If dn represents the nth digit of the fractional part, find the value of the following expression.
d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''

import itertools

def getDigit(index):
    # Make it 0-offset
    real_index = index - 1

    # The first set is 1-9 = 9 * 1 digits
    # The second is 10-99 = 90 * 2 digits
    # The third is 100-999 = 900 * 3 digits
    # The kth set is 9 * 10**(k-1) * k digits
    
    # The 1st set ends at 9 * 1
    # The 2nd set ends at 9 * 21
    # The 3rd set ends at 9 * 321

    end = 0
    for k in itertools.count(1):
        prev_end = end
        end += 9 * k * 10 ** (k-1)
        if end > real_index:
            break

    # Now k is the index of the set we're in, and end is the end of our set
    # prev_end is the end of the previous set
    set_index = real_index - prev_end

    nth_value = set_index / k

    value = 10**(k - 1) + nth_value

    value_str = str(value)

    digit_str = value_str[set_index % k]

    return digit_str

import Util

print (Util.prod( [int(getDigit(i)) for i in [ 1, 10, 100, 1000, 10000, 100000, 1000000 ] ] ))
