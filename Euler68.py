import itertools

# Project Euler #68, Magic 5-gon ring

# Let's begin by solving for the 3-gon ring.

# We basically have a collection of 6 numbers, and we add together certain combinations of the numbers to form a total.
# Represent the ring as an array, with associated collections of indices representing the lines we add to form a total


#     0
#      \
#       1
#      / \
#     2 - 3 - 4
#    /
#   5

# Note the direction of indices must go clockwise
sample_ring = [4, 3, 1, 2, 6, 5]

class Ring:
    total_indices = [ (0, 1, 3), (4, 3, 2), (5, 2, 1) ]
    def __init__(self, values):
        self.values = values
        self._build_ring()

    def _build_ring(self):
        assert(self.values)
        self.tuples = [ tuple(self.values[i] for i in indices) for indices in self.total_indices ]
       
    def __str__(self):
        return '  {}\n   \\\n    {}\n   / \\\n  {} - {} - {}\n /\n{}'.format(*self.values)

    def number_string(self):
        return ''.join(str(x) for y in self.tuples for x in y)

    # A ring is in unique form if the first tuple starts with the lowest external node
    def is_unique_form(self):
        return self.tuples[0] == min(self.tuples)

    # the common sum of each tuple, or None if there is no common sum
    def total(self):
        result = sum(self.tuples[0])
        if all(result == sum(n) for n in self.tuples):
            return result
        else:
            return None

#    0
#     \\
#       1    2
#     // \\ /
#    3     4
#  // \   /
# 5    6-7-8
#       \
#        9
class Ring5:
    total_indices = [ (0, 1, 4), (2, 4, 7), (8, 7, 6), (9, 6, 3), (5, 3, 1) ]
    def __init__(self, values):
        self.values = values
        self._build_ring()

    def _build_ring(self):
        assert(self.values)
        self.tuples = [ tuple(self.values[i] for i in indices) for indices in self.total_indices ]
       
    def __str__(self):
        return \
r"""   {}
    \\
      {}    {}
    // \\ /
   {}     {}
 // \   /
{}    {}-{}-{}
      \
       {}""".format(*self.values)

    def number_string(self):
        return ''.join(str(x) for y in self.tuples for x in y)

    # A ring is in unique form if the first tuple starts with the lowest external node
    def is_unique_form(self):
        return self.tuples[0] == min(self.tuples)

    # the common sum of each tuple, or None if there is no common sum
    def total(self):
        result = sum(self.tuples[0])
        if all(result == sum(n) for n in self.tuples):
            return result
        else:
            return None

max_string = '0'
for ring in itertools.permutations(range(1, 7)):
    r = Ring(ring)
    if not r.is_unique_form():
        continue

    total = r.total()
    if not total:
        continue

    print(r)
    print(r.tuples)
    print(total)
    print(r.number_string())
    
    num_string = r.number_string()
    if len(num_string) != 9:
        continue

    if num_string > max_string:
        max_string = num_string

print(max_string)

max_string = '0'
for ring in itertools.permutations(range(1, 11)):
    r = Ring5(ring)
    if not r.is_unique_form():
        continue


    total = r.total()
    if not total:
        continue

    print(r)
    print(r.tuples)
    print(total)
    print(r.number_string())
    
    num_string = r.number_string()
    if len(num_string) != 16:
        continue

    if num_string > max_string:
        max_string = num_string

print(max_string)
