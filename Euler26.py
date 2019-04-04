# Reciprocating demoninators problem
# Find the value n<1000 with the longest reviprocating denominator

import itertools

''' Sample program to long-divide a number.  Just for reference.
n = 382

# print 1/382

dividend = 1

print ("0.")

while (dividend != 0):
  print (dividend // n)
  dividend = dividend % n * 10
'''

def divisors(n):
  ''' Return the remainders of the long division of 1/n'''
  dividend = 1

  while (dividend != 0):
    remainder = dividend % n
    yield remainder
    dividend = remainder * 10

max = (0, None)

for i in range (1, 1000):
  history = dict()
  for currstep, remainder in zip (itertools.count(), divisors(i)):
    print ('loop: ' + str((currstep, remainder)))
    if remainder == 0:
      print ((i, 0))
      break
    elif remainder in history:
      cycle_len = currstep - history[remainder]
      if cycle_len > max[0]:
        max = (cycle_len, i)
      print ((i, currstep - history[remainder]))
      break
    else:
      history[remainder] = currstep

print ('Max is ' + str(max))
