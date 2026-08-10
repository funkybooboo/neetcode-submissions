from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n: int = len(nums)
        r: int = n
        
        for i in range(n):
            r += i - nums[i]

        return r
