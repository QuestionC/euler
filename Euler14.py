from array import array

cache = dict()

cache[1] = 1;

def collatz(i: int):
    if i in cache:
        return cache[i]
    else:
        result = collatz(int(i/2)) if i % 2 == 0 else collatz(i * 3 + 1)
        result += 1
        cache[i] = result
        return result


max = (0, 0)

for i in range (1, 1000000):
    c = collatz(i)
    if c > max[0]:
        max = (c, i)

print (str(max))
