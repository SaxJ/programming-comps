def calcBumps(k, m):
    if k == 0:
        return 1
    for i in range(m):


class Solution:
    def numOfArrays(self, n, m, k):
        if n < k or m < k:
            return 0
        else:
            nBumps = calcBumps(k)
