import Util
import itertools

pair_sets = [ [], [], [], [], []  ]

def grow_set(N, p):
    if N == 0:
        pair_sets[0].append((p,))
        return

    for ps in pair_sets[N - 1]:
        for y in ps:
            if not is_pair(p, y):
                break
        else:
            pair_sets[N].append(ps + (p,))

pairs = set()
def is_pair(a, b):
    # print ('Is Pair {} {}'.format(a, b))
    if (a,b) in pairs:
        return True
    
    if a % 3 + b % 3 == 3:
        return False

    c = str(a) + str(b)
    d = str(b) + str(a)

    if Util.is_prime(int(c)) and Util.is_prime(int(d)):
        pairs.add((a, b))
        return True


for p in Util.primes():
    before = len(pair_sets[3])
    grow_set(4, p)
    grow_set(3, p)
    grow_set(2, p)
    grow_set(1, p)
    grow_set(0, p)

    for s in pair_sets[3][before:]:
        print(s)

    if len(pair_sets[4]) > 0:
        print (pair_sets[4])
        break

exit()


X = Util.next_primes(14)
for _ in range(10):
    print(next(X))
quit()

# Find 5 primes such that any concatenation of 2 is also prime.

# Find N primes such that any concatenation of 2 is also prime.
def pair_sets(N):
    if N == 1:
        for p in primes():
            yield (p,)
    else:
        X = pair_sets(N)
        for pair_set in X:
            last = pair_set[-1]
            primes = next_primes(last + 1)
            for p in primes:
                for p2 in pair_set:
                    if not is_pair(p, p2):
                        break
                


def my_combinations(iterable, r):
    if r == 1:
        for x in iterable:
            yield (x,)
    else:
        old = []
        for _ in range(r-1):
            old.append(next(iterable))

        new = next(iterable)

        while True:
            '''
            for x in itertools.combinations(old, r - 1):
                yield x + (new,)
            '''
            for x in my_combinations(iter(old), r - 1):
                for y in x:
                    if not is_pair(y, new):
                        break
                else:
                    yield x + (new,)

            old.append(new)
            new = next(iterable)
            if new == None:
                break


def prime_pair(N):
    for a in intertools.combinations(Util.primes()):
        print(a)

for x in my_combinations(Util.primes(), 3):
    print(x)
