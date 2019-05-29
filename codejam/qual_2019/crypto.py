from math import gcd
from string import ascii_uppercase

T = int(input())
for t in range(T):
    [n, l] = [int(x) for x in input().split(' ')]
    cypher = [int(x) for x in input().split(' ')]
    primesFound = []
    for i, curr in enumerate(cypher):
        if i == len(cypher) - 1:
            break
        p = gcd(curr, cypher[i + 1])
        primesFound.append(p)

    primesFound.insert(0, cypher[0] // primesFound[0])
    primesFound.append(cypher[-1] // primesFound[-1])
    alpha = list(ascii_uppercase)
    uniquePrimes = sorted(list(set(primesFound)))
    charMap = dict(zip(uniquePrimes, alpha))
    decoded = ''.join([charMap[x] for x in primesFound])

    print('Case #{}: {}'.format(t + 1, decoded))
