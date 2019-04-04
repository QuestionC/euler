import itertools
import Util 

def pandigitals(i):
    as_string = ''.join( str(k) for k in range (i, 0, -1))

    return (itertools.permutations(as_string))

# Original version
for i in range (9, 0, -1):
    for j in pandigitals(i):
        d = int(''.join(j))

        if Util.is_prime(d):
            print (d)
            break
    else:
        continue # Gross
    break

# Get rid of the ugly break
for d in (int(''.join(j)) for i in range(9, 0, -1) for j in pandigitals(i)) :
    if Util.is_prime(d):
        print(d)
        break

# What I expected to work (doesn't)
'''
for j in pandigitals(i) for i in range(9, 0, -1):
    d = int(''.join(j))
        
    if Util.is_prime(d):
        print (d)
        break
'''
