T = int(input())
for t in range(T):
    nSessions, numToAdd = [int(x) for x in input().split()]
    times = [int(x) for x in input().split()]
    diffs = []
    for i in range(1, nSessions):
        diffs.append(times[i] - times[i - 1])
    print(diffs)
