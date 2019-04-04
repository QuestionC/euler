# The fraction 49/98 is a curious fraction as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8 whcih is correct, is obtained by cancelling the 9s.

# We shall consider fractions like 30/50 = 3/5 to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms, find the value of the denominator

# Represent each fraction as a tuple
# Each fraction is less than one, so the numerator is smaller than the dominator
# Numerator and denominator are at least two digits each

import itertools
from Util import lcm 
from Util import gcd

def reduce (numerator, denominator):
    g = gcd(numerator, denominator)
    return (numerator // g, denominator // g)


result = (1, 1)

for numerator, denominator in itertools.combinations (range(10, 100), 2):
  # Skip the trivial case of '0'
  if '0' in itertools.chain(str(numerator), str(denominator)): continue

  # Skip the trivial case of '11', '22'
  # if str(numerator)[0] == str(numerator

  for i in str(numerator):
    if i in str(denominator):
      numerator_list = list(str(numerator))
      denominator_list = list(str(denominator))

      numerator_list.remove(i)
      denominator_list.remove(i)

      new_numerator = int(''.join(numerator_list))
      new_denominator = int(''.join(denominator_list))
        
      if (reduce (new_numerator, new_denominator) == reduce (numerator, denominator)):      
        print ((numerator, denominator))
        result = ( result[0] * numerator, result[1] * denominator)

print (result)
print (reduce(result[0], result[1]))
