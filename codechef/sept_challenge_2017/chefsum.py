T = int(input())

for t in range(T):
    n = int(input())
    xs = [int(x) for x in input().split(' ')]
    
    suffix = sum(xs)
    prefix = xs[0]
    minSum = suffix + prefix
    minI = 1
    for i in range(2, n+1):
        suffix = suffix - xs[i-2]
        prefix = prefix + xs[i-1]
        sm = suffix + prefix
        if sm < minSum:
            minSum = sm
            minI = i

    print(minI)
