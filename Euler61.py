import itertools

# Begin: Calculate the figurate numbers in range [1000,10000)

def figurate(N):
    # Figurate numbers follow a pattern
    for X in itertools.count(1):
        yield ((N - 2) * X * X + (4 - N) * X) // 2

fig_thousands = {}

for N in range(3, 9):
    fig_thousands[N] = []

    X = figurate(N)
    for x in X:
        if x > 9999:
            break

        if x > 999:
            if x % 100 > 9: # Third digit can't be 0
                fig_thousands[N].append(x)

# End: Calculate the figurate numbers in range

# N is the preceeding number
# fig_order is an iterator of figurate ranks we need to use
def construct_cycle(N, fig_order):
    # print ('construct_cycle {} {}'.format(N, fig_order))

    # Try every possible next number
    # The next number starts with the last 2 digits of N
    first_digits = N % 100

    curr_fig = fig_order[0]

    result = []
    for X in fig_thousands[curr_fig]:
        if X > first_digits * 100 and X < (first_digits + 1) * 100:

            if len(fig_order) == 1:
                # We're on the last element
                T = [(X,)]
            else:
                S = construct_cycle(X, fig_order[1:])
                T = [(X,) + k for k in S]

            result.extend(T)

    # print ('construct_cycle {} {} returning {}'.format(N, fig_order, result))
    return result

# We need every possible permutation of the numbers 3 thru 7.
# 8 is implied first
perm_base = [N for N in range(3, 8)]
perms = list(itertools.permutations(perm_base))

for E in fig_thousands[8]:
    for P in perms:
        S = construct_cycle(E, P)

        for s in S:
            print('{} {} {}'.format(E, s, P))
            if s[-1]%100 == E//100:
                exit()
