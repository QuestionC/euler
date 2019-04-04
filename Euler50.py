from Util import primes
from itertools import count
from Util import is_prime

for length in count (2):
    window = []
    total = 0
    for p in primes():
        # If the window is full, we need to drop the first element
        if len(window) == length:
            total -= window[0]
            window.pop(0)
        
        # In any case, we need to increase total and grow the window.
        total += p
        window.append(p)
        
        # If we overflow the value, we're done
        if total >= 1000000:
            break

        # If the window is full with a prime, we need to record it and stop
        if len(window) == length and is_prime(total):
            max = (total, len(window))
            print (max)
            break

    if len(window) < length:
        # We had to break out due to overflow before the window was full.
        # Length has gone too far
        break

print (max)
