from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return min(nums)

        left = 0
        right = len(nums) - 1
        if nums[left] < nums[right]:
            return nums[left]
        right = 1
        while right < len(nums) and nums[left] < nums[right]:
            left += 1
            right += 1
        return nums[right]
