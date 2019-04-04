val = 600851475143

curr = 2

while curr < val:
    while val % curr == 0:
        val /= curr
        print (str(curr) + ", " + str(val))
    curr += 1

