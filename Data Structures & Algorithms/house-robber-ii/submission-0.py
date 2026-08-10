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
        if n == 3:
            return max(nums[0], max(nums[1], nums[2]))

        def rob_linear(start: int, end: int) -> int:
            memo = [-1] * n

            def max_rob_from(i: int) -> int:
                if i > end:
                    return 0
                if memo[i] != -1:
                    return memo[i]

                skip = max_rob_from(i + 1)
                rob = nums[i] + max_rob_from(i + 2)

                memo[i] = max(skip, rob)
                return memo[i]

            return max_rob_from(start)

        # Case 1: Rob from house 0 to n-2
        # Case 2: Rob from house 1 to n-1
        return max(rob_linear(0, n - 2), rob_linear(1, n - 1))
