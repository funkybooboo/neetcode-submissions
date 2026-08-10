from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        memo = [-1] * n

        def max_rob_from(i: int) -> int:
            if i >= n:
                return 0
            if memo[i] != -1:
                return memo[i]

            # Option 1: Skip current house
            skip = max_rob_from(i + 1)
            # Option 2: Rob current house and skip next
            rob = nums[i] + max_rob_from(i + 2)

            memo[i] = max(skip, rob)
            return memo[i]

        return max_rob_from(0)
