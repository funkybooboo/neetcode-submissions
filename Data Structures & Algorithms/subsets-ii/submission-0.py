from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = set()
        subset = []
        def helper(i):
            if i >= len(nums):
                result.add(tuple(subset.copy()))
                return
            subset.append(nums[i])
            helper(i + 1)
            subset.pop()
            helper(i + 1)
        nums.sort()
        helper(0)
        return [list(r) for r in result]
