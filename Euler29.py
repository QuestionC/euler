from Util import primes

result_set = set()

for a in range (2, 101):
    for b in range(2, 101):
        result_set.add(a**b)

print (len(result_set))

