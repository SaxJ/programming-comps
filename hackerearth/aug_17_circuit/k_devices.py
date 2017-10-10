import math

(N, K) = [int(x) for x in input().split(' ')]
Xs = [int(x) for x in input().split(' ')]
Ys = [int(x) for x in input().split(' ')]

coords = list(zip(Xs, Ys))

def dist(x,y):
    return math.sqrt(x * x + y * y)

dists = [dist(a[0], a[1]) for a in coords]
dists.sort()
print(math.ceil(dists[K-1]))

