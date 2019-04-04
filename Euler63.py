import itertools

total = 0

for N in range(1, 10):
    for power in itertools.count(1):
        L = len(str(N ** power))
        
        print ('{} {} {}'.format(power, N, L))

        if L == power:
            total += 1
        if L < power:
            break

print(total)
