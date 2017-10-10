T = int(input())

for t in range(T):
    problems, people = [int(x) for x in input().split(' ')]
    solved = [int(x) for x in input().split(' ')]

    cake = 0
    hard = 0
    for n in solved:
        if n >= people // 2:
            cake += 1

        if n <= people // 10:
            hard += 1

    if cake == 1 and hard == 2:
        print("yes")
    else:
        print("no")
