def next(node, grid):
    ns = []
    for n in len(grid):
        if grid[node][n] is not None:
            ns.append(n)
    return ns

N, M, S = [int(x) for x in input().split(' ')]
edges = [[None] * N] * N 
for m in range(M):
    u, v, a, b = [int(x) for x in input().split(' ')]
    edges[u-1][v-1] = (a, b) # (cost, time)
    edges[v-1][u-1] = (a, b) # (cost, time)

exchanges = {}
waits = {}
for i in range(N):
    c, d = [int(x) for x in input().split(' ')]
    exchanges[i] = c
    waits[i] = d

for destination in range(1, N):
    stack = []
    path = {}

    ns = next(0, edges)

    while len(stack) > 0:
        
