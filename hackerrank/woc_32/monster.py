nMonsters, hit, t = [int(x) for x in input().split(' ')]

monsters = [int(x) for x in input().split(' ')]
monsters.sort()

killed = 0
timeLeft = t
for m in monsters:
    toKill = m // hit
    if toKill == 0:
        toKill = 1
    elif m % hit != 0:
        toKill += 1

    #print(str(m) + '-' + str(toKill))
    
    if toKill <= timeLeft:
        killed += 1
        timeLeft -= toKill

print(killed)
