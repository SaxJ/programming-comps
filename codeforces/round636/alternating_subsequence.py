def opposite(x, y):
    if (x < 0 and y < 0) or (x > 0 and y > 0):
        return False
    else:
        return True

T = int(input())
for t in range(T):
    n = int(input())
    nums = [int(x) for x in input().split(' ')]
    total = nums[0]
    head = nums[0]
    for n in nums[1:]:
        if opposite(head, n):
            total += head
            head = n
        else:
            if n > head:
                head = n
            
    print(total)
