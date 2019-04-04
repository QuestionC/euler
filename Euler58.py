# Project Euler problem 58
# Spiralling primes
import itertools
import bisect
import math

primes = [2, 3, 5]


def prime(N):
    global primes

    ''' Return the N'th prime. 2 is the 0th prime'''
    if N < len(primes):
        return primes[N]

    for j in range (len(primes), N + 1):
        for x in itertools.count(primes[-1]+1):
            is_prime = True

            for p in primes:
                if x % p == 0:
                    is_prime = False
                    break

            if is_prime:
                primes.append(x)
                break

    return primes[N]

def isPrime(N):
    while N > primes[-1]:
        prime(len(primes))
    
    pos = bisect.bisect_left(primes, N)
    # print ('{} {} {}'.format(N, primes, pos))
    if (primes[pos] == N):
        return True
    return False

isPrime(100)

def isPrime2(N):
    '''
    for p in primes:
        if p == N:
            return True
        if N % p == 0:
            return False

    for k in range(primes[-1], int(math.sqrt(N))):
        if N % k == 0:
            return False
    '''

    if N == 1:
        return False

    for k in range(2, int(math.sqrt(N)) + 1):
        if N % k == 0:
            return False

    return True


# Ring 0 is 1
# Ring 1 is 3 5 7 9
# Ring 2 is 13 17 21 25
def ring(N):
    if N == 0:
        return [1]
    k = 2 * N + 1
    square = k * k
    delta = 2 * N
    return [square - 3 * delta, square - 2 * delta, square - delta, square]

hits = 0
miss = 0

for R in itertools.count():
    corners = ring(R)
    for C in corners:
        if (isPrime2(C)):
            hits += 1
        else:
            miss += 1

    if R > 2 and hits / (hits + miss) < .1:
        print(R)
        break

    print ('{} {} {}'.format(R, hits / (hits + miss), len(primes)))



