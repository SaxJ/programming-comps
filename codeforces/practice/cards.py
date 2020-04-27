n = int(input())
s = input()

counts = {
    'z':0,
    'e':0,
    'r':0,
    'o':0,
    'n':0
}

for c in s:
    counts[c] += 1

ones = min(counts['o'], counts['n'], counts['e'])

counts['o'] -= ones
counts['n'] -= ones
counts['e'] -= ones

zeros = min(counts['z'], counts['e'],counts['r'], counts['o'])
z = ['0'] * zeros
o = ['1'] * ones
print(' '.join(o + z))
