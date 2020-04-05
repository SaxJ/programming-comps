#!/usr/bin/env python3

def factors(n):
    result = set()
    for i in range(1, int(n ** 0.5) + 1):
        div, mod = divmod(n, i)
        if mod == 0:
            result |= {i, div}
    return result

n = int(input())
print(len(factors(n)) - 1)
