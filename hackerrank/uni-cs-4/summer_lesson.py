#!/bin/python3

import os
import sys


#
# Complete the howManyStudents function below.
#
def howManyStudents(m, c):
    # Return an array denoting the number of students taking each class.
    seen = {}
    for idx, v in enumerate(c):
        if v in seen:
            seen[v] += 1
        else:
            seen[v] = 0
            
    ret = []
    for i in range(m):
        if i in seen:
            ret.append(seen[i])
        else:
            ret.append(0)
    return ret


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = howManyStudents(m, c)

    f.write(' '.join(map(str, result)))
    f.write('\n')

    f.close()
