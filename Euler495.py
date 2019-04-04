def factor (x):
    result = dict()

    i = 2
    while i * i <= x:
        while x % i == 0:
            if i not in result:
                result[i] = 0
            result[i] += 1
    i += 1

def foo (a: int, b: int):
    return 5

print (str(foo (3, 4)))
