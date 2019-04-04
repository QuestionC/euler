# 192 x (1, 2, 3) = (192, 384, 576) which joins into a pandigital
# 9 x (1, 2, 3, 4, 5) = (9, 18, 27, 36, 45)
# What is the largest pandigital number that can be formed this way where the tuple is (1, 2, ..., n) for n > 1?

import itertools

max = 0

for n in range (2, 10):
    y = tuple(range(1, n + 1))

    for x in itertools.count():
        z_tuple = tuple (i * x for i in y)
        z_string = ''.join (str(i) for i in z_tuple)
        if len(z_string) > 9:
            #print ((x, y, z_string))
            break
        if sorted(z_string) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print ((x, y, z_string)) 
            if int(z_string) > max:
                max = int(z_string)

print (max)
