from typing import List
import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        pivot = random.choice(nums)
        left = [x for x in nums if x < pivot]
        mid  = [x for x in nums if x == pivot]
        right = [x for x in nums if x > pivot]
        return self.sortArray(left) + mid + self.sortArray(right)
