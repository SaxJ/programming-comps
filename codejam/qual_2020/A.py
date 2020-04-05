#!/usr/bin/env python3

T = int(input())
for t in range(T):
    N = int(input())
    cols = [{} for n in range(N)]
    badCols = [0 for x in range(N)]
    badRows = [0 for x in range(N)]
    trace = 0
    for r in range(N):
        row = [int(x) for x in input().split(' ')]
        seen = {}
        for c, v in enumerate(row):
            if v not in cols[c]:
                cols[c][v] = True
            else:
                badCols[c] = 1
            if v not in seen:
                seen[v] = True
            else:
                badRows[r] = 1
            if r == c:
                trace += v

    rt = sum(badRows)
    ct = sum(badCols)
    print("Case #{}: {} {} {}".format(t+1, trace, rt, ct))
        
