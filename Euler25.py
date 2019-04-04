a = 1
b = 1
i = 1

while a < 10**999:
    i += 1
    temp = a + b
    a = b
    b = temp

print (i, a)
