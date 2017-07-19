nCases = int(input())

def addSnake(toAdd, snakes):
    for i, s in enumerate(snakes):
        if s > toAdd:
            snakes.insert(i, toAdd)
            return
    snakes.append(toAdd)

for c in range(nCases):
    nSnakes, nQueries = [int(x) for x in input().split(' ')]
    lengths = [int(x) for x in input().split(' ')]
    lengths.sort()

    for q in range(nQueries):
        goal = int(input())
        hungry = lengths[0]
        maxI = -1
        fail = True
        for i, s in enumerate(lengths):
            if i == 0:
                continue

            if hungry >= goal:
                fail = False
                break

            maxI = i
            hungry = max(s, hungry) + 1
        count = nSnakes - maxI
        if hungry < goal:
            print(0)
        else:
            print(count)
