from math import sqrt

def divisor_sum (x):
    if x == 1: return 1
    return sum ( i for i in range (1, x) if x % i == 0 )


amicable_sum = 0
for i in range (1, 10000):
    d = divisor_sum(i)
    if i != d and i == divisor_sum(d):
        print (i)
        amicable_sum += i

print (amicable_sum)
