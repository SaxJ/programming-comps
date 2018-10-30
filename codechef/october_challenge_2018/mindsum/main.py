def digitsum(n):
    return sum([int(x) for x in str(n)])

def bfs(n, d, seen):
    nxt = [(n, 0)]
    small = n
    path = 0
    while nxt:
        curr, p = nxt.pop()
        if curr < small:
            small = curr
            path = p

        if curr in seen:
            return seen[curr]

        seen[curr] = (small, path)
        nxt.append((digitsum(curr), p + 1))
        nxt.append((curr + d, p + 1))

cases = int(input())
for c in range(cases):
    n, d = [int(x) for x in input().split()]
    print(bfs(n, d, {}))
