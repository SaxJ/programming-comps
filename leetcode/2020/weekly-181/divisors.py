import math

class Solution:
    def divisors(self, n):
        output = set()
        i = 1
        while i <= math.sqrt(n):
            if n % i == 0:
                output.add(i)
                output.add(n // i)
            i += 1
        return output

    def sumFourDivisors(self, nums):
        sums = 0
        for n in nums:
            divs = self.divisors(n)
            if len(divs) == 4:
                sums += sum(divs)
        return sums
