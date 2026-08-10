from typing import List, Dict, Tuple


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache: Dict[Tuple[int, int], int] = {}
        def dfs(i: int, sum: int) -> int:
            nonlocal nums, target

            if (i, sum) in cache:
                return cache[(i, sum)]

            if i >= len(nums):
                return 1 if sum == target else 0

            cache[(i, sum)] = dfs(i + 1, sum + nums[i]) + dfs(i + 1, sum - nums[i])
            return cache[(i, sum)]

        return dfs(0, 0)
