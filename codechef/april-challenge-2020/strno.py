import math
factorsCache = {}

def factors(n):    
    if n in factorsCache:
        return factorsCache[n]
    
    result = set()
    for i in range(1, int(n ** 0.5) + 1):
        div, mod = divmod(n, i)
        if mod == 0:
            result |= {i, div}

    result = sorted(list(filter(lambda x: x != 1, result)))
    factorsCache[n] = result
    return result

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n%2 == 0:
        return False
    if n < 9:
        return True
    if n%3 == 0:
        return False

    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0:
            return False
        if n%(f+2) == 0:
            return False

        f +=6
    return True    

def product(xs):
    total = 1
    for x in xs:
        total *= x
    return total

def findTuples(goal, chosen, depth, k):
    if depth == k and product(chosen) == goal:
        return chosen
    
    fs = factors(goal)
    for f in fs:
        nxt = product(chosen) * f
        if nxt > goal:
            return None
        else:
            return findTuples(goal, chosen + [f], depth + 1, k)
            

T = int(input())
for t in range(T):
    x, k = [int(x) for x in input().split(' ')]
    tup = findTuples(x, [], 0, k)
    if tup is not None:
        print(1)
    else:
        print(0)
