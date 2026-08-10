from typing import List, Dict


class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        nums = [1] + nums + [1]
        n: int = len(nums)
        cache: List[List[int]] = [[0] * n for _ in range(n)]

        for length in range(2, n):
            for left in range(n - length):
                right = left + length

                for i in range(left + 1, right):
                    cache[left][right] = max(
                        cache[left][right],
                        nums[left] * nums[i] * nums[right] + cache[left][i] + cache[i][right],
                    )

        return cache[0][n - 1]
