import itertools

with open('Euler59.txt') as f:
    cipher = [int(k) for k in f.read().split(',')]

# Space and 'e' are gonna be the most common values

# The password is 3 characters
chunks = zip(*zip(*[iter(cipher)]*3))

print(cipher)

chunks = [sorted(a) for a in chunks]

def list2counts(N):
    result = {}

    for a in N:
        if a in result:
            result[a] += 1
        else:
            result[a] = 1

    return result

chunks = [list2counts(a) for a in chunks]

def biggest2(N):
    b1k = None
    b1v = 0
    b2k = None
    b2v = 0

    for a in N:
        if N[a] > b1v:
            b2k = b1k
            b2v = b1v
            b1k = a
            b1v = N[a]
        elif N[a] > b2v:
            b2k = a
            b2v = N[a]

    return (b1k, b2k)

biggest = [biggest2(a) for a in chunks]

print(biggest)

'''
71,2
79,7
68,1
First is space (32), second is e(101)

xor values are 103, 98 or 111, 102 or 100
'''

message = ''
total = 0

for x in zip(cipher, itertools.cycle([103, 111, 100])):
    message += chr(x[0] ^ x[1])
    total += x[0] ^ x[1]

print(message)
print(total)
