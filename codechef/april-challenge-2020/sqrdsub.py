T = int(input())
for t in range(T):
    N = int(input())
    nums = [int(x) for x in input().split(' ')]
    current = 1
    count = 0
    for x in nums:
        current *= x
        if current * x ==
