T = int(input())
for t in range(T):
    n, m = [int(x) for x in input().split(" ")]
    grid = []
    white = 0
    black = 0

    for i in range(n * m):
        if i % 2 == 0:
            black += 1
            grid.append("B")
        else:
            white += 1
            grid.append("W")

    for i, c in enumerate(grid):
        if c == "W" and white > black - 1:
            print("B", end="")
            white -= 1
        else:
            print(c, end="")
        if (i + 1) % m == 0 and i > 0:
            print()
