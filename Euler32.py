result_set = set()

def ispandigital(x, y, z):
    full_str = str(x) + str(y) + str(z)
    return ''.join(sorted(full_str)) == "123456789"

for x in range (1, 10):
    for y in range (1000, 10000):
        z = x * y
        if ispandigital(x, y, z):
            result_set.add(z)
            print (str((x, y, z)))

for x in range (10, 100):
    for y in range (100, 1000):
        z = x * y
        if x == 39 and y == 186:
            print (str((x, y, z)))
        if ispandigital(x, y, z):
            result_set.add(z)
            print (str((x, y, z)))

print (sum(result_set))
