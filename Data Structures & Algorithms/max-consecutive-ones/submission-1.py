from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count: int = 0
        current_count: int = 0

        for num in nums:
            if num == 1:
                current_count += 1
            else:
                if current_count > max_count:
                    max_count = current_count
                current_count = 0

        if current_count > max_count:
            max_count = current_count

        return max_count
