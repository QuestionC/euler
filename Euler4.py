max = (0, 0, 0)
for i in range (100, 999):
    for j in range (i, 999):
        product = i * j

        as_string = str(product)


        for x, y in zip (as_string, reversed(as_string)):
            if x != y:
                break
        else:
            print (str(i) + ", " + str(j) + ", " + str(product))
            if product > max[2]:
                max = (i, j, product)
print ("Highest was " + str(max[0]) + ", " + str(max[1]) + ", " + str(max[2]))
