# If p is perimeter of right angle triangle with sides {a, b, c}, there are 3 solutions for p=120...
# {20, 48, 52}, {24, 45, 51}, {30, 40, 50}
# For what value p<= 1000 are there the most solutions

# So, clearly we're looking for cases where sum(a, b, sqrt(a**2 + b**2)) == p
# Square roots suck so mathemagic that into 0 == p**2 + 2ab - 2pa - 2pb
# b = (p**2 - 2pa) / (2p - 2a)
# b is integral if (p**2 - 2pa) % (2p - 2a) is 0

maxcount = (0, None)
for p in range(1001):
    count = 0
    for a in range (1, p):
        if (p * p - 2 * p * a) % (2 * p - 2 * a) == 0:
            print ((a, p))
            count += 1
    if count > maxcount[0]:
        maxcount = count, p

print (maxcount)

