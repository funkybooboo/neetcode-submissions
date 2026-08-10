from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self._search_helper(nums, target, 0, len(nums) - 1)

    def _search_helper(self, nums: List[int], target: int, left: int, right: int) -> int:
        if left > right:
            return -1

        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self._search_helper(nums, target, mid + 1, right)
        else:
            return self._search_helper(nums, target, left, mid - 1)
