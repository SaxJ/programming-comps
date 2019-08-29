import math

divs = {}
def divisors(n):
    return [x for x in range(1, math.ceil(math.sqrt(n))) if n % x == 0]

T = int(input())
for t in range(T):
    print('=================')
    nPeople, nDays = [int(x) for x in input().split(' ')]
    healths = [int(x) for x in input().split(' ')]
    damage = [int(x) for x in input().split(' ')]

    deaths = []
    for i, health in enumerate(healths):

