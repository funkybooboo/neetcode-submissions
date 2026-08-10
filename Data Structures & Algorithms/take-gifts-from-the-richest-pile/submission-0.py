import heapq
import math
from typing import List

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # negate to make a max heap
        max_heap = [-g for g in gifts]
        heapq.heapify(max_heap)

        for _ in range(k):
            largest = -heapq.heappop(max_heap)
            reduced = int(math.isqrt(largest))  # faster than sqrt + floor
            heapq.heappush(max_heap, -reduced)

        return -sum(max_heap)
