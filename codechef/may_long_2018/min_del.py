from fractions import gcd
def checkArray(arr):
    i = 0
    j = 1
    while i != j:
        if gcd(nums[i], nums[j]) != 1:
            if len(arr) > 2:
                del nums[i]
            return False
        i += 1
        j += 2
        j = j % len(arr)
    return True

T = int(input())
for t in range(T):
    removed = 0
    N = int(input())
    nums = [int(x) for x in input().split(' ')]
    
    done = False
    while not done:
        check = checkArray(nums)
        if len(nums) == 2 and not check:
            break
        elif not check:
            removed += 1
        else:
            done = True

    if done:
        print(removed)
    else:
        print(-1)
