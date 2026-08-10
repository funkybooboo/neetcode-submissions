from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0 if target == nums[0] else -1
        left = 0
        right = len(nums) - 1
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        if nums[left] < nums[right]:
            return self._b_search(nums, target)

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] > target or nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[mid] > target or nums[right] < target:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1

    def _b_search(self, nums: List[int], target: int) -> int:
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
