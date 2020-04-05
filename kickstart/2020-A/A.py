T = int(input())
for t in range(T):
    (N, B) = [int(x) for x in input().split(' ')]
    costs = [int(x) for x in input().split(' ')]
    costs.sort()
    count = 0
    total = 0
    for i in costs:
        newTotal = total + i
        if newTotal > B:
            print("Case #{}: {}".format(t+1, count))
            break
        else:
            count += 1
            total = newTotal
