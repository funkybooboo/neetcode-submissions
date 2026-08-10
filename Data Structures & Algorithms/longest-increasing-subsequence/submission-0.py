from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        memo = [1] * n  # memo[i] = length of LIS ending at index i
        max_length = 1

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    memo[i] = max(memo[i], memo[j] + 1)
            max_length = max(max_length, memo[i])

        return max_length
