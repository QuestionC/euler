matrix = []

with open('Euler11.txt') as f:
#with open('Euler11_test.txt') as f:
    for i in f.readlines():
        matrix.append( [ int(x) for x in i.split() ] )

maxprod = 0

def prod (x):
    curr = 1
    for i in x:
        curr *= i
    return curr, x

maxside = max (  prod ( [ matrix[i + x][j] for x in range(4) ] ) for i in range(len(matrix) - 3) for j in range (len(matrix[0])))

maxvert = max ( prod ( [matrix[i][j + x] for x in range(4) ] ) for i in range(len(matrix)) for j in range (len(matrix[0]) - 3))

maxdiag = max ( prod ( [matrix[i + x][j + x] for x in range(4) ] ) for i in range(len(matrix) - 3) for j in range (len(matrix[0]) - 3))

maxotherdiag = max (prod ( [matrix[i + x][j - x] for x in range(4) ] ) for i in range(len(matrix) - 3) for j in range (3, len(matrix[0])))

print ( max ((maxside, maxvert, maxdiag, maxotherdiag)) )
