n = int(input())
notes = 0
for d in [100,20,10,5,1]:
    notes += n // d
    n = n % d
print(notes)
