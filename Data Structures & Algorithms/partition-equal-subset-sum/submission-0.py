from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        # If total sum is odd, it can't be partitioned equally
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2
        n = len(nums)
        memo = {}

        def dfs(index: int, current_sum: int) -> bool:
            # If we've hit the target, partition is possible
            if current_sum == target:
                return True
            # If we've gone out of bounds or exceeded the target, stop
            if index >= n or current_sum > target:
                return False
            # Check cache
            if (index, current_sum) in memo:
                return memo[(index, current_sum)]

            # Explore both options: skip or include current number
            include = dfs(index + 1, current_sum + nums[index])
            skip = dfs(index + 1, current_sum)

            result = include or skip
            memo[(index, current_sum)] = result  # Cache result
            return result

        return dfs(0, 0)
