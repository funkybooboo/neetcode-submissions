from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        goal_index: int = len(nums) - 1

        def find_max(left_index: int, right_index: int) -> int:
            max_value: int = 0
            for index in range(left_index, right_index):
                value = nums[index]
                if value > max_value:
                    max_value = value
            return max_value

        count: int = 0
        left_index: int = 0
        right_index: int = 1

        while right_index <= goal_index:  # Ensure the loop runs until right_index reaches the goal_index
            max_jump = find_max(left_index, right_index)
            if max_jump == 0:
                return 0
            left_index = right_index  # Update left_index to the new right_index
            right_index = min(right_index + max_jump, goal_index + 1)  # Move right_index forward by the max_jump, but do not exceed the goal_index
            count += 1

        return count
