from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        def dfs(i: int, acc: int):
            if i == len(nums):
                return acc
            return (
                    dfs(i + 1, acc) + # skip i
                    dfs(i + 1, acc ^ nums[i]) # take i
            )

        return dfs(0, 0)