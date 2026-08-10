from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        goal_index: int = len(nums) - 1

        def find_farthest(left_index: int, right_index: int) -> int:
            max_reach: int = 0
            for index in range(left_index, right_index):
                reach = index + nums[index]
                if reach > max_reach:
                    max_reach = reach
            return max_reach

        count: int = 0
        left_index: int = 0
        right_index: int = 1

        while right_index <= goal_index:
            farthest = find_farthest(left_index, right_index)
            if farthest <= left_index:
                return 0
            count += 1
            left_index = right_index
            right_index = min(farthest + 1, goal_index + 1)

        return count
