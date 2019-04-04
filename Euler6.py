sumofsquares = 0
squareofsum = 0

for i in range(101):
    sumofsquares += i * i
    squareofsum += i

squareofsum *= squareofsum

print (str(squareofsum - sumofsquares))

