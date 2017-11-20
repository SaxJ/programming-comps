T = int(input())

for t in range(T):
    N, K = [int(x) for x in input().split(' ')]
    nums = [int(x) for x in input().split(' ')]
    numSet = set(nums)
    maxNum = max(nums)

    fullSet = set(list(range(0, maxNum)))
    leftSet = fullSet - numSet
    left = list(leftSet)

    if len(left) == 0:
        add = maxNum
        for i in range(K):
            add += 1
            numSet.add(add)
    else:
        add = maxNum
        for i in range(K):
            if len(left) > 0:
                numSet.add(left.pop(0))
            else:
                add += 1
                numSet.add(add)

    
    maxNum = max(numSet)
    fullSet = set(list(range(0, maxNum)))
    leftSet = fullSet - numSet

    if len(leftSet) == 0:
        print(maxNum + 1)
    else:
        print(min(leftSet))
