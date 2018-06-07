# Given a list of prices, where index is minutes after 9am, and value at that index is the price,
# determine the maximum profit that could be made.

def maxProf(prices):
    profit = 0
    lowest = prices[0]
    for p in prices[1:]:
        if p > lowest:
            diff = p - lowest
            if diff > profit:
                profit = diff
        else:
            lowest = p
    return profit

prices = [10, 7, 5, 8, 11, 9]
print(maxProf(prices))
