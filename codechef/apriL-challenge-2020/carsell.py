T = int(input())
for t in range(T):
    N = int(input())
    prices = sorted([int(x) for x in input().split(' ')], reverse=True)

    total = 0
    for subtract, price in enumerate(prices):
        total += max(0, price - subtract)
    print(total % 1000000007)
