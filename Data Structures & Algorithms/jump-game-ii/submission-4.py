from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # The last index we want to reach
        goal_index = len(nums) - 1

        # Helper function to find the farthest index we can reach
        # from the current jump window [left_index, right_index)
        def find_farthest_index(left_index: int, right_index: int) -> int:
            max_reach = 0
            for index in range(left_index, right_index):
                # Calculate how far we can jump from this index
                reach = index + nums[index]
                max_reach = max(max_reach, reach)
            return max_reach

        # Number of jumps made so far
        jump_count = 0

        # Current range of indices we can jump from
        left_index = 0
        right_index = 1

        # While the right edge of our jump range hasn't passed the goal
        while right_index <= goal_index:
            # Find the farthest index we can reach from the current jump window
            farthest_index = find_farthest_index(left_index, right_index)

            # If we can't move forward, the goal is unreachable (shouldn't happen in valid input)
            if farthest_index <= left_index:
                return 0

            # We've used one more jump to extend our range
            jump_count += 1

            # Move the window to the next range
            left_index = right_index
            right_index = min(farthest_index + 1, goal_index + 1)

        return jump_count
