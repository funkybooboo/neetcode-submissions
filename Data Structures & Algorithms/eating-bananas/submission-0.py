from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            if self._can_finish(piles, h, mid):
                right = mid  # try a smaller k
            else:
                left = mid + 1  # need a bigger k

        return left

    def _can_finish(self, piles: List[int], h: int, k: int) -> bool:
        total_hours = 0
        for pile in piles:
            total_hours += math.ceil(pile / k)
        return total_hours <= h
