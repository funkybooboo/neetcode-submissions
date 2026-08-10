from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self._search_matrix_helper(matrix, target, 0, len(matrix) - 1)

    def _search_matrix_helper(self, matrix: List[List[int]], target: int, left: int, right: int) -> bool:
        if left > right:
            return False

        mid = (left + right) // 2

        nums = matrix[mid]

        if self._search_helper(nums, target, 0, len(nums) - 1):
            return True
        elif nums[(len(nums) - 1) // 2] < target:
            return self._search_matrix_helper(matrix, target, mid + 1, right)
        else:
            return self._search_matrix_helper(matrix, target, left, mid - 1)


    def _search_helper(self, nums: List[int], target: int, left: int, right: int) -> bool:
            if left > right:
                return False

            mid = (left + right) // 2

            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                return self._search_helper(nums, target, mid + 1, right)
            else:
                return self._search_helper(nums, target, left, mid - 1)
