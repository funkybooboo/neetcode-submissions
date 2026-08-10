from typing import List, Tuple

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        memo: List[Tuple[int, int, int]] = [None] * n  # (max_ending, min_ending, max_so_far)

        def dfs(i: int) -> Tuple[int, int, int]:
            if memo[i] is not None:
                return memo[i]

            if i == 0:
                memo[i] = (nums[0], nums[0], nums[0])
                return memo[i]

            prev_max, prev_min, prev_result = dfs(i - 1)
            curr = nums[i]

            max_ending = max(curr, curr * prev_max, curr * prev_min)
            min_ending = min(curr, curr * prev_max, curr * prev_min)
            max_so_far = max(prev_result, max_ending)

            memo[i] = (max_ending, min_ending, max_so_far)
            return memo[i]

        return dfs(n - 1)[2]
