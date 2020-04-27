T = int(input())
for t in range(T):
    N = int(input())
    a = [int(x) for x in input().split(" ")]
    b = [int(x) for x in input().split(" ")]
    possible = True

    for j in range(N):
        goal = b[j]

        found = False
        lastDiff = 1000000000000
        total = 0
        if a[j] == b[j]:
            continue
        while total != goal:
            progress = False
            for i in range(j, -1, -1):
                current = a[j] + a[i]
                if abs(goal - total) > abs(goal - (total + current)):
                    progress = True
                    total += current
                    continue
            if not progress:
                break

        found = total == goal
        if not found:
            break
    if possible:
        print("YES")
    else:
        print("NO")
