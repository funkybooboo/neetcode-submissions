from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        goal: int = len(nums) - 1

        def find_max(left_index: int, right_index) -> int:
            max_value: int = 0
            for index in range(left_index, right_index):
                value = nums[index]
                if value > max_value:
                    max_value = value
            return max_value

        count: int = 0
        left_index: int = 0
        right_index: int = 1

        while right_index <= goal:
            value = find_max(left_index, right_index)
            if value == 0:
                return 0
            left_index = right_index
            right_index += value
            count += 1

        return count
