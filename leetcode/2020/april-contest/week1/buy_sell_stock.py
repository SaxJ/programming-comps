class Solution:

    def maxDiff(self, arr):
        return max(arr) - min(arr)

    def maxProfit(self, prices):
        last = None
        root = None
        profit = 0
        for i, p in enumerate(prices):
            if last is None:
                last = p
            else:
                if p < last:
                    last = p
                else:
                    profit += p - last
                    last = None
        return profit
