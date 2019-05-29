T = int(input())

for t in range(T):
    N = int(input())
    moves = input()
    myMoves = []
    for m in moves:
        if m == 'E':
            myMoves.append('S')
        else:
            myMoves.append('E')
    print("Case #{}: {}".format(t + 1, ''.join(myMoves)))
