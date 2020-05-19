import math

T = int(input())
for t in range(T):
    n = int(input())

    angle = (((2 * math.pi) / (2 * n)) / 2)

    toFlat = 0.5 / math.sin(angle)

    print(2 * toFlat)
