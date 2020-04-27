T = int(input())
for t in range(T):
    n = int(input())
    skills = [int(x) for x in input().split(" ")]
    if n == 1:
        print(0)
        continue
    groups = {}
    maxGroup = 0
    maxSkill = None
    distinct = set()
    for skill in skills:
        if skill in distinct:
            if skill not in groups:
                groups[skill] = 0
            groups[skill] += 1
            if groups[skill] > maxGroup:
                maxGroup = groups[skill]
                maxSkill = skill
        distinct.add(skill)

    if len(distinct) - 1 > maxGroup:
        maxGroup += 1
    print(max(1, maxGroup))
