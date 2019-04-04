from array import array

f = open('p067_triangle.txt', 'r')
# f = open ('Euler67_test.txt', 'r')

heap = []

global max_depth 
max_depth = 0

for linenum, line in enumerate(f.readlines()):
    max_depth = linenum

    for inner_index, x in enumerate(line.split()):
        value = int(x)

        index = len(heap)

        left_parent = index - linenum - 1
        right_parent = index - linenum

        if linenum == 0:
            # Root node
            heap.append (value)
        elif inner_index == 0:
            print (str(value) + ' has no left parent.  using rig')
            # No left parent.  Just use right parent.
            heap.append (heap[right_parent] + value)
        elif inner_index == linenum:
            print (str(value) + ' has no right parent')
            # No right parent.
            heap.append (heap[left_parent] + value)
        else:
            heap.append (value + max (heap[left_parent], heap[right_parent]))

max_left = int(max_depth * (max_depth + 1) / 2)
max_right = max_left + max_depth + 2

print ( str ( (max_depth, max_left, max_right) ) )

# heap[] now contains each element's distance.  Find the max of the lowest row
print ( str (max (heap[max_left : max_right] ) ) )

