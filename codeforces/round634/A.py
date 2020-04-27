T = int(input())
for t in range(T):
    n = int(input())
    if n % 2 == 0:
        even = n // 2
        print(even - 1)
    else:
        print(n // 2)
