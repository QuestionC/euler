from itertools import count

def spiral(N):
    if N == 1: return 1
    else:
        base = (2 * N - 1) **2
        delta = -(2 * (N - 1))
        print ((base, delta))
        return sum (base + delta * x for x in range(4))

print (sum (spiral(x) for x in range(1, 502)))
