T = int(input())
for t in range(T):
    program = input()

    mults = []
    diffs = [(0, 0)]

    for c in program:
        if c == "(":
            diffs.append((0, 0))
        elif c == ")":
            m = mults.pop()
            dx, dy = diffs.pop()
            x, y = diffs[-1]
            x += dx * m
            y += dy * m
            diffs[-1] = (x, y)
        elif c.isdigit():
            mults.append(int(c))
        else:
            x, y = diffs[-1]
            if c == "N":
                y -= 1
            elif c == "S":
                y += 1
            if c == "E":
                x += 1
            if c == "W":
                x -= 1
            diffs[-1] = (x, y)

    x, y = diffs[-1]
    x = 1 + (x % 1000000000)
    y = 1 + (y % 1000000000)
    print("Case #{}: {} {}".format(t + 1, x, y))
