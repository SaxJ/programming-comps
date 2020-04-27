moves = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}

T = int(input())
for t in range(T):
    X, Y = [int(x) for x in input().split(" ")]
    ns = []
    ns.append((1, 0, 0, ""))
    ns.append((1, -1, 0, "W"))
    ns.append((1, 1, 0, "E"))
    ns.append((1, 0, 1, "N"))
    ns.append((1, 0, -1, "S"))

    found = False
    while len(ns) != 0:
        step, x, y, p = ns.pop(0)
        nStep = 2 * step
        if x == X and y == Y:
            print("Case #{}: {}".format(t + 1, p))
            found = True
            break
        elif abs(x) > abs(X) or abs(y) > abs(Y):
            continue
        else:
            for d in moves:
                dx, dy = moves[d]
                xx = x + dx * nStep
                yy = y + dy * nStep
                if abs(xx) <= 1000000000 and abs(yy) <= 1000000000:
                    ns.append((nStep, x + dx * nStep, y + dy * nStep, p + d))

    if not found:
        print("Case #{}: {}".format(t + 1, "IMPOSSIBLE"))
