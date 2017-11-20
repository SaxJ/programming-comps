height, width = [int(x) for x in input().split(' ')]
board = []
for i in range(height):
    board.append([int(x) for x in input().split(' ')])

topAndBottomCount = 0
for i in range(height):
    for j in range(width):
        if board[i][j] > 0:
            topAndBottomCount += 1

topAndBottom = 2 * topAndBottomCount
print(topAndBottom)

northSouthCount = 0
for j in range(width):
    mx = 0
    for i in range(height):
        a = board[i][j]
        if a > mx:
            mx = a
    northSouthCount += mx
    print("mx col = {}".format(mx))
northSouth = 2 * northSouthCount
print(northSouth)

eastWestCount = 0
for i in range(height):
    mx = 0
    for j in range(width):
        a = board[i][j]
        if a > mx:
            mx = a
    eastWestCount += mx
    print("mx row = {}".format(mx))
eastWest = 2 * eastWestCount
print(eastWest)

print(eastWestCount * 2 + northSouthCount * 2 + topAndBottom)
