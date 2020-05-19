import math

T = int(input())

for t in range(T):
    a, b, c, d = [int(x) for x in input().split(' ')]
    if b >= a:
        print(b)
        continue

    if d >= c:
        print("-1")
        continue

    remaining = a - b
    perUnit = c - d
    units = math.ceil(remaining / perUnit)
    print(b + c * units)
