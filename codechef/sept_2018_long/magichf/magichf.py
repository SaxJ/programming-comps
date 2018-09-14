T = int(input())

for t in range(T):
    n, x, s = [int(x) for x in input().split()]
    for i in range(s):
        a, b = [int(x) for x in input().split()]
        if a == x:
            x = b
        elif b == x:
            x = a
    print(x)
