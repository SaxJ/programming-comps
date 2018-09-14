T = int(input())
for t in range(T):
    n, m, x, y = [int(x) for x in input().split()]
    N = (n - 1) // x
    M = (m - 1) // y
    reachedN = x * N + 1
    reachedM = y * M + 1
    if n <= 2 and m <= 2:
        print('Chefirnemo')
        continue
    if (abs(reachedN - n) == 0 and abs(reachedM - m) == 0) or (abs(reachedN - n) == 1 and abs(reachedM - m) == 1):
        print('Chefirnemo')
    else:
        print('Pofik')
