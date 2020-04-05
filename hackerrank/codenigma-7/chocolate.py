#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the chocolateFeast function below.
def chocolateFeast(n, c, m):
    chocs = n // c
    wrappers = 0
    total = 0
    new = 1
    while new > 0:
        new = chocs // m
        left = chocs % m
        if new == 0:
            total += left
            break
        total += new * m
        chocs = new + left
    return total

t = int(input())

for t_itr in range(t):
    ncm = input().split()

    n = int(ncm[0])

    c = int(ncm[1])

    m = int(ncm[2])

    result = chocolateFeast(n, c, m)
    print(result)
