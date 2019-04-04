# Find the sum of all numbers that can be written as the sum of fifth powers of their digits.

nums = '0123456789'

# 9**5 = 59049, so the highest number of possible digits is gonna be 6 since 9999999 -> 413343, we can't generate 7 digit number with 5 digits.

import itertools

totaltotal = 0

for possible in itertools.combinations_with_replacement(nums, 7):
  total = sum ( [ int(i)**5 for i in possible ] )

  if total in [ int(''.join(x)) for x in itertools.permutations(possible) ]:
    print (total)
    totaltotal += total

#print ((possible, total))
print (totaltotal)
