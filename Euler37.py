# 3797 is an interesting number because 3797, 797, 97, and 7 are all prime.  So are 3, 37, 379.

# Find the sum of the only eleven primes with this property.
# 2, 3, 5, and 7 don't count

# All truncable primes are 1 digit bigger than another truncable prime, or 2, 3, 5, 7.
# So start at 2, 3, 5, and 7.  Then try to generate new truncable primes by sticking new numbers (which must be 2, 3, 5, and 7) on the left and right sides.

# Let's split the idea into two concepts, left truncable and right truncable.
# You generate any left truncable prime by putting a prime on the left of a left truncable prime

# You generate any right truncable prime by putting a prime on the right of a right truncable prime

from Util import is_prime
import string 

right_trunc = left_trunc = ['2', '3', '5', '7']

dual_trunc = []

while (True):
    print ('R: ' + str(right_trunc))
    print ('L: ' + str(left_trunc))
    next_right = []
    for i in right_trunc:
        # What you gonna do with all that junk? All that junk inside yo' trunc?
        # Thank you, I'll be here all night.
        for p in string.digits:
            next_val = int(i + p)
            if is_prime(next_val):
                next_right.append(str(next_val))

    # Shameful copy paste
    next_left = []
    for i in left_trunc:
        # What you gonna do with all that junk? All that junk inside yo' trunc?
        # Thank you, I'll be here all night.
        for p in string.digits:
            next_val = int (p + i)
            if is_prime(next_val):
                next_left.append(str(next_val))

    dual_trunc.extend (set(next_left) & set(next_right))
    print (dual_trunc)

    if len(dual_trunc) == 11: 
        print (sum([int(i) for i in dual_trunc]))
        exit()

    left_trunc = next_left
    right_trunc = next_right
