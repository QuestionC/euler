import math

N = 23

root = math.sqrt(N)

# The numerator must be at least root - A
A = math.floor(root)

numerator_tail = A
denominator = N - A * A

val = N + A / D + 1
numerator_tail -= val * denominator


# Convert N to (A, B) where A * A + B = N and A is floor(sqrt(N))
def convert(N):
    A = math.floor(math.sqrt(N))
    B = N - A * A
