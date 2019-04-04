# Find a * b | |a|<1000 and |b|<1000 and n**2 + a*n + b produces the maximum number of primes for consecutive n starting with n=0

import itertools
from Util import is_prime

max = (0, None, None)

for a, b in itertools.product(range (-1000, 1001), range(-1000, 1001)):
  for n in itertools.count():
    test_me = n**2 + a * n + b;
    if test_me < 2  or not is_prime (n**2 + a * n + b):
#print ((n, a, b, test_me))
      if n > max[0]:
        max = (n, a, b)
      break

print (max)
print (max[1] * max[2])
