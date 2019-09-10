a = list(range(1,101))
while len(a) > 1:
    print(a)
    a = [x for (i, x) in enumerate(a) if (i + 1) % 2 == 0]

print(a)
