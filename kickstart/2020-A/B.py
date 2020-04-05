plates = []
N, K, P = [0, 0, 0]

def tree(stack, depth):
    if depth >= K - 1:
        return plates[stack][-1]
    else:
        return max([tree(i, )])

T = int(input())
for t in range(T):
    (N, K, P) = [int(x) for x in input().split(' ')]
    for r in range(N):
        stack = [int(x) for x in input().split(' ')]
        plates.append(stack)

    soln = max([tree(i, 0) for i, _ in enumerate(plates)])
