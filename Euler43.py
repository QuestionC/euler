# Project Euler problem 43

import itertools

s = set('0123456789')

total = 0

# This is either horrible or beautiful.
for d8, d9, d10 in itertools.permutations(s, 3):
    as_str = d8 + d9 + d10
    if int(as_str) % 17 == 0:
        leftover7 = s.difference(as_str)
        for d7 in leftover7:
            as_str = d7 + d8 + d9
            if int(as_str) % 13 == 0:
                leftover6 = leftover7.difference(d7)
                for d6 in leftover6:
                    as_str = d6 + d7 + d8
                    if int(as_str) % 11 == 0:
                        leftover5 = leftover6.difference(d6)
                        for d5 in leftover5:
                            as_str = d5 + d6 + d7
                            if int(as_str) % 7 == 0:
                                leftover4 = leftover5.difference(d5)
                                for d4 in leftover4:
                                    as_str = d4 + d5 + d6
                                    if int(as_str) % 5 == 0:
                                        leftover3 = leftover4.difference(d4)
                                        for d3 in leftover3:
                                            as_str = d3 + d4 + d5
                                            if int(as_str) % 3 == 0:
                                                leftover2 = leftover3.difference(d3)
                                                for d1, d2 in itertools.permutations(leftover2):
                                                    as_str = d2 + d3 + d4
                                                    if int(as_str) % 2 == 0:
                                                        if d1 != 0: # Leading zeroes don't count as pandigital
                                                            as_str = d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9 + d10
                                                            total += int(as_str)
                                                            print(as_str)

print(total)
