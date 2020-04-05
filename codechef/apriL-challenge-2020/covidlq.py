T = int(input())
for t in range(T):
    N = int(input())
    queue = [int(x) for x in input().split(' ')]
    last = -1
    fail = False
    for idx, q in enumerate(queue):
        if q == 0:
            continue
        else:
            if last == -1:
                last = idx
                continue
            diff = idx - last
            if diff < 6:
                fail = True
                break
            last = idx
    if not fail:
        print("YES")
    else:
        print("NO")
                
