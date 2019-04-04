i = 0
j = 1

def fib():
    global i
    global j
    new = i + j
    i = j
    j = new

total = 0

while j < 4000000:
    if j%2 == 0:
        total += j
        print (str(j) + ", " + str(total))

    fib()

