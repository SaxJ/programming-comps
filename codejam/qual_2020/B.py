import math

T = int(input())
for t in range(T):
    s = [int(x) for x in input()]
    result = ''
    last = 0
    for n in s:
        diff = n - last
        if diff > 0:
            result += '(' * diff
            result += str(n)
        elif diff < 0:
            result += ')' * int(math.fabs(diff))
            result += str(n)
        else:
            result += str(n)
        last = n
    result += ')' * last
    print("Case #{}: {}".format(t+1, result))
