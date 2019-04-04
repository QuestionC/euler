# Let's try the brute force way.
import itertools
import math

count = 0

for c in range(1, 100000):
    for b in range(int(math.sqrt(c)), c):
        a = int(math.sqrt(c*c - b*b))
        if a*a + b*b == c*c:
            count += 1
            if count % 1000 == 0:
                print ((count, a, b, c))
            # print((a, b, c))
