from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        def helper(i):
            if i >= len(nums):
                result.append(subset.copy())
                return
            subset.append(nums[i])
            helper(i + 1)
            subset.pop()
            helper(i + 1)
        helper(0)
        return result
