class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        output = []
        for i, n in enumerate(nums):
            output.insert(index[i], n)
        return output
