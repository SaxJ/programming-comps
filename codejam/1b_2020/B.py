e9 = 1000000000
T, A, B = [int(x) for x in input().split(" ")]
averageRadius = A + B

x = -e9 + averageRadius
y = -e9 + averageRadius
blocks = (2 * e9) // averageRadius

for t in range(T):
    done = False
    hit = False

    for i in range(blocks):
        for j in range(blocks):
            nx = x + i * averageRadius
            ny = y + j * averageRadius
            print("{} {}".format(nx, ny))
            ans = input()
            if ans == "CENTER":
                done = True
                break
            elif ans == "HIT":
                x = nx
                y = ny
                hit = True
                break
            else:
                continue
        if hit or done:
            break
    # found circle at this point
