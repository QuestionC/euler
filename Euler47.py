from itertools import count
from Util import factor

fourfacts = []

for i in count(1):
    if sum(1 for i in factor(i)) == 4:
        fourfacts.append(i)
        if len(fourfacts) >= 4 and fourfacts[-4] == i - 3:
            print (fourfacts[-4])
            break

