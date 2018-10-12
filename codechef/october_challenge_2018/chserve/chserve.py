cases = int(input())
for c in range(cases):
    a, b, k = [int(x) for x in input().split()]
    chef = a // k
    cook = b // k
    d = abs(chef - cook)
    rems = (a % k) + (b % k)
    extra = rems // k
    switches = d + extra
    if switches % 2 == 0:
        print('CHEF')
    else:
        print('COOK')
