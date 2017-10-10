T = int(input())
for test in range(T):
    n = int(input())

    avail = list(range(1, n+1))
    perm = []
    for i in range(1, n+1):
        for ix, c in enumerate(avail):
            if c == i:
                continue
            else:
                perm.append(avail.pop(ix))
                break

    if len(avail) > 0:
        perm.insert(len(perm) - 1, avail[0])

    items = [str(x) for x in perm]
    print(' '.join(items))

