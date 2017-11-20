N = int(input())

minName = "-1"
minCost = 10000000000

for i in range(N):
    name, amount = input().split(' ')

    fours = 0
    sevens = 0
    valid = True
    for c in amount:
        if c == '4':
            fours += 1
        elif c == '7':
            sevens += 1
        else:
            valid = False
            break

    if fours == sevens and valid:
        amountInt = int(amount)
        if amountInt < minCost:
            minName = name
            minCost = amountInt

print(minName)
