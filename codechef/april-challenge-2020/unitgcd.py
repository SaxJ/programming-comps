import math

cache = {}
def makeFrom(n, until):
    start = n
    if n in cache:
        start = max(cache[n])
    else:
        cache[n] = set()

    soFar = cache[n]
    for i in range(start, until + 1):
        valid = True
        for ii in soFar:
            if math.gcd(ii, i) != 1:
                valid = False
                break
        if valid:
            soFar.add(i)
    return soFar

T = int(input())
for t in range(T):
    N = int(input())
    seqs = []
    seen = set()
    all = set(range(1, N+1))
    
    while len(seen) < N:
        notSeen = all - seen
        pages = makeFrom(min(notSeen), N)
        seen = seen.union(pages)
        seqs.append(pages)

    print(len(seqs))
    for s in seqs:
        print_pages = ' '.join([str(x) for x in s])
        print("{} {}".format(len(s), print_pages))
    
