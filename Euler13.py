with open('Euler13.txt') as f:
    lines = f.readlines();
    print (str(lines))
    result = sum ( [ int(line) for line in lines ] )
    print (str(result), len(str(result)))
