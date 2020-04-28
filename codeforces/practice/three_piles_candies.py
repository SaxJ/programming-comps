Q = int(input())
for q in range(Q):
    a, b, c = [int(x) for x in input().split(' ')]
    ans = (a + b + c) // 2
    print(ans)
