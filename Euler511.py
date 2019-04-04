import Util

n = 1234567898765
k = 4321

x = Util.factor(n)

# Project Euler problem 511
# This isn't so bad because the factors are just 5, 41, 25343, and 237631

factors = [  5, 41, 25343, 237631 ]

import itertools
# From python itertools recipies
def powerset(iterable):
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))

fac_mods = []
for i in powerset(factors):
    remainder1 = [aa for aa in factors if aa not in i]
    factor1 = Util.prod(i)

    fac_mods.append((factor1, factor1 % k))

# Generate each combination of k numbers that add up to n
def ways2add (n, k, append_to_me=[]):
    if k == 1:
        append_to_me.append(n)
        yield append_to_me
        append_to_me.pop()
    else:
        for i in range(n):
            append_to_me.append(i)
            for i in ways2add (n - i, k - 1, append_to_me):
                yield i
            append_to_me.pop()

for i in ways2add(n, 2):
    print (i)
