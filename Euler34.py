# 145 = 1! + 4! + 5!

# Find the sum of all numbers which are equal to thesum of their factorial of digits

# 9! * 7 and 9! * 8 are 7 digits long, so the answer is at most 7 digits
from math import factorial
import itertools 

vals = dict( [ (i, factorial(i)) for i in range(0, 10) ] )

for num_digits in range (2, 8):
  for i in itertools.combinations_with_replacement (vals.keys(), num_digits):
    fact_total = sum ( [ vals[j] for j in i ] )
   
    '''
    print (sorted ([ int(k) for k in str(fact_total) ] ) )
    print (i)
    '''
    
    if list(i) == sorted ([ int(k) for k in str(fact_total) ] ):
      print (fact_total)
