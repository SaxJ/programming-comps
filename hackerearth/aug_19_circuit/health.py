T = int(input())
for t in range(T):
    print('=================')
    nPeople, nDays = [int(x) for x in input().split(' ')]
    healths = [int(x) for x in input().split(' ')]
    damage = [int(x) for x in input().split(' ')]

    days = [-1] * (nPeople)
    for day in range(nDays):
        mult = 1
        while (day + 1) * mult <= nPeople:
            person = ((day + 1) * mult) - 1
            if healths[person] <= damage[day]:
                if days[person] == -1:
                    days[person] = day + 1
            mult = mult + 1

    for x in days:
        print(x)
