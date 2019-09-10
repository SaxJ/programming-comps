fibs = [0, 1]
for i in range(2, 100):
    fibs.append(fibs[i-1] + fibs[i-2])
mod = [x % 10 for x in fibs]

print(mod[:60])
print('---')
print(mod[60:])
