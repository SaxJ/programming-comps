class Solution:
    def isHappy(self, n):
        digits = [int(x) for x in str(n)]
        bads = set([4, 16, 37, 58, 89, 145, 42, 20])
        while True:
            squares = sum([int(x)*int(x) for x in digits])
            if squares == 1:
                return True
            if squares in bads:
                return False
            digits = [int(x) for x in str(squares)]
