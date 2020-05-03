T = int(input())
for t in range(T):
    n, d = [int(x) for x in input().split(' ')]
    angles = [int(x) for x in input().split(' ')]

    counts = {}
    maxCount = 0
    maxAngle = None
    left = 360 * (10 ** 9)

    for a in angles:
        left -= a
        if a not in counts:
            counts[a] = 1
        else:
            counts[a] += 1

    if counts[a] > maxCount:
        maxCount = counts[a]
        maxAngle = a

    remaining = d - maxCount
    if remaining <= 0:
        print("Case #{}: {}".format(t + 1, 0))
        continue



