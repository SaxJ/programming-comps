import math

T = int(input())
for t in range(T):
    n = int(input())

    angle = ((360 / (2 * n)) / 2) * (math.pi / 180)
    toFlat = 0.5 / math.tan(angle)

    print(2 * toFlat)
