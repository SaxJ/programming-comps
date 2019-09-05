rubles = int(input())
d = int(input())
e = int(input())

# 1 dollar bills go into all other notes
# 5 euro bills go into the others
bestLeft = rubles
i = 1
while i * d <= rubles:
    dollarsLeft = rubles - (i * d)
    bestLeft = min(bestLeft, dollarsLeft % (5 * e))
    i = i + 1

print(bestLeft)
