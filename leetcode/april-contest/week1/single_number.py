#!/usr/bin/env python3

class Solution:
    def singleNumber(self, nums):
        seen = {}
        for n in nums:
            if n in seen:
                seen.remove(n)
            else:
                seen.add(n)
        return seen.pop()
