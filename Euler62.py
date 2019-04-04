import Util
import itertools

def is_cube(N):
    for X in Util.factor(N):
        if X[1] % 3 != 0:
            return False
    return True

tracker = {}
threshold = 10

for N in itertools.count(1):
    cube = N**3

    if cube > threshold:
        for N in tracker:
            if tracker[N][1] == 5:
                print(tracker[N])

        # print(threshold)
        # print(tracker)
        tracker = {}
        threshold *= 10

    s_cube = ''.join(sorted(str(cube)))

    if s_cube in tracker:
        tracker[s_cube][1] += 1
    else:
        tracker[s_cube] = [cube, 1]

