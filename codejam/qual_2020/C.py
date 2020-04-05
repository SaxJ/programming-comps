T = int(input())
for t in range(T):
    nActivities = int(input())
    activities = []

    idx = 0
    for a in range(nActivities):
        s, e = [int(x) for x in input().split(' ')]
        activities.append((s, e, idx))
        idx += 1

    activities.sort(key=lambda x: x[0])
    impossible = False
    assigned = {}
    assigns = []
    for (s, e, i) in activities:
        if 'C' in assigned and s >= assigned['C']:
            assigned.pop('C')
        if 'J' in assigned and s >= assigned['J']:
            assigned.pop('J')

        if 'C' in assigned and 'J' in assigned:
            impossible = True
            break
        if 'C' not in assigned:
            assigns.append((i, 'C'))
            assigned['C'] = e
        elif 'J' not in assigned:
            assigns.append((i, 'J'))
            assigned['J'] = e

    assigns.sort(key=lambda x: x[0])
    assigns = [c for (i, c) in assigns]
        

    if impossible:
        print("Case #{}: {}".format(t+1, "IMPOSSIBLE"))
    else:
        print("Case #{}: {}".format(t+1, ''.join(assigns)))
